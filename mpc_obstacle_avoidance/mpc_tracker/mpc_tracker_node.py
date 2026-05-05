#!/usr/bin/env python3
import math
import numpy as np
import cvxpy as cp
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path, Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def yaw_from_quat(q):
    return math.atan2(2.0 * (q.w * q.z), 1.0 - 2.0 * (q.z * q.z))


class MPCTrackerNode(Node):
    def __init__(self):
        super().__init__('mpc_tracker_node')
        p = self.declare_parameter
        self.odom_topic = p('odom_topic', '/odom').value
        self.scan_topic = p('scan_topic', '/scan').value
        self.cmd_topic = p('cmd_topic', '/cmd_vel').value
        self.path_topic = p('smoothed_path_topic', '/smoothed_path').value
        self.N = int(p('horizon', 12).value)
        self.dt = float(p('dt', 0.15).value)
        self.max_v = float(p('max_v', 0.6).value)
        self.max_w = float(p('max_w', 1.2).value)
        self.goal_tol = float(p('goal_tolerance', 0.2).value)
        self.safety_radius = float(p('safety_radius', 0.55).value)
        self.corridor_width = float(p('corridor_width', 0.6).value)
        self.lookahead = float(p('dynamic_obstacle_lookahead', 2.8).value)
        self.lateral_shift_max = float(p('lateral_shift_max', 1.4).value)
        self.lateral_shift_step = float(p('lateral_shift_step', 0.2).value)

        self.sub_path = self.create_subscription(Path, self.path_topic, self.path_cb, 10)
        self.sub_odom = self.create_subscription(Odometry, self.odom_topic, self.odom_cb, 20)
        self.sub_scan = self.create_subscription(LaserScan, self.scan_topic, self.scan_cb, 20)
        self.pub_cmd = self.create_publisher(Twist, self.cmd_topic, 20)
        self.timer = self.create_timer(self.dt, self.control_loop)

        self.path_xy = np.empty((0, 2))
        self.state = np.zeros(3)
        self.have_odom = False
        self.obstacles = np.empty((0, 2))
        self.last_u = np.array([0.0, 0.0])

    def path_cb(self, msg):
        self.path_xy = np.array([[p.pose.position.x, p.pose.position.y] for p in msg.poses], dtype=float)

    def odom_cb(self, msg):
        self.state[0] = msg.pose.pose.position.x
        self.state[1] = msg.pose.pose.position.y
        self.state[2] = yaw_from_quat(msg.pose.pose.orientation)
        self.have_odom = True

    def scan_cb(self, msg):
        if not self.have_odom:
            return
        pts = []
        angle = msg.angle_min
        for r in msg.ranges:
            if msg.range_min < r < min(msg.range_max, self.lookahead):
                lx, ly = r * math.cos(angle), r * math.sin(angle)
                c, s = math.cos(self.state[2]), math.sin(self.state[2])
                gx = self.state[0] + c * lx - s * ly
                gy = self.state[1] + s * lx + c * ly
                pts.append((gx, gy))
            angle += msg.angle_increment
        self.obstacles = np.array(pts, dtype=float) if pts else np.empty((0, 2))

    def nearest_index(self):
        if len(self.path_xy) == 0:
            return 0
        d = np.linalg.norm(self.path_xy - self.state[:2], axis=1)
        return int(np.argmin(d))

    def build_reference(self, idx0):
        ref = []
        for k in range(self.N + 1):
            i = min(idx0 + k, len(self.path_xy) - 1)
            x, y = self.path_xy[i]
            if i < len(self.path_xy) - 1:
                dx, dy = self.path_xy[i + 1] - self.path_xy[i]
            else:
                dx, dy = self.path_xy[i] - self.path_xy[i - 1]
            yaw = math.atan2(dy, dx)
            ref.append((x, y, yaw))
        return np.array(ref)

    def path_blocked(self, ref):
        if len(self.obstacles) == 0:
            return False
        for rx, ry, _ in ref:
            d = np.linalg.norm(self.obstacles - np.array([rx, ry]), axis=1)
            if np.any(d < self.safety_radius + self.corridor_width * 0.5):
                return True
        return False

    def local_detour(self, ref):
        if len(self.obstacles) == 0:
            return ref
        for shift in np.arange(self.lateral_shift_step, self.lateral_shift_max + 1e-6, self.lateral_shift_step):
            for sign in (+1.0, -1.0):
                cand = ref.copy()
                for i in range(len(cand)):
                    yaw = cand[i, 2]
                    nx, ny = -math.sin(yaw), math.cos(yaw)
                    cand[i, 0] += sign * shift * nx
                    cand[i, 1] += sign * shift * ny
                ok = True
                for rx, ry, _ in cand:
                    d = np.linalg.norm(self.obstacles - np.array([rx, ry]), axis=1)
                    if np.any(d < self.safety_radius):
                        ok = False
                        break
                if ok:
                    return cand
        return ref

    def solve_mpc(self, ref):
        x = cp.Variable((3, self.N + 1))
        u = cp.Variable((2, self.N))
        cost = 0
        cons = [x[:, 0] == self.state]
        for k in range(self.N):
            yaw_r = ref[k, 2]
            v_r = 0.35
            A = np.eye(3)
            A[0, 2] = -self.dt * v_r * math.sin(yaw_r)
            A[1, 2] = self.dt * v_r * math.cos(yaw_r)
            B = np.array([
                [self.dt * math.cos(yaw_r), 0.0],
                [self.dt * math.sin(yaw_r), 0.0],
                [0.0, self.dt],
            ])
            cons += [x[:, k + 1] == A @ x[:, k] + B @ u[:, k]]
            cons += [cp.abs(u[0, k]) <= self.max_v, cp.abs(u[1, k]) <= self.max_w]
            q = np.diag([12.0, 12.0, 2.0])
            r = np.diag([0.2, 0.15])
            e = x[:, k] - ref[k, :]
            cost += cp.quad_form(e, q) + cp.quad_form(u[:, k], r)
            if k > 0:
                cost += 0.1 * cp.sum_squares(u[:, k] - u[:, k - 1])

        cost += cp.quad_form(x[:, self.N] - ref[self.N, :], np.diag([15.0, 15.0, 3.0]))
        prob = cp.Problem(cp.Minimize(cost), cons)
        prob.solve(solver=cp.OSQP, warm_start=True, verbose=False)
        if u.value is None:
            return np.array([0.0, 0.0])
        return np.array([u.value[0, 0], u.value[1, 0]])

    def control_loop(self):
        if not self.have_odom or len(self.path_xy) < 2:
            return
        idx = self.nearest_index()
        if np.linalg.norm(self.path_xy[-1] - self.state[:2]) < self.goal_tol:
            self.pub_cmd.publish(Twist())
            return

        ref = self.build_reference(idx)
        if self.path_blocked(ref):
            ref = self.local_detour(ref)

        cmd = self.solve_mpc(ref)
        tw = Twist()
        tw.linear.x = float(np.clip(cmd[0], -self.max_v, self.max_v))
        tw.angular.z = float(np.clip(cmd[1], -self.max_w, self.max_w))
        self.pub_cmd.publish(tw)


def main(args=None):
    rclpy.init(args=args)
    node = MPCTrackerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
