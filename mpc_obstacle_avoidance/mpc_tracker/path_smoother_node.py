#!/usr/bin/env python3
import numpy as np
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from scipy.interpolate import splprep, splev


class PathSmootherNode(Node):
    def __init__(self):
        super().__init__('path_smoother_node')
        self.input_topic = self.declare_parameter('input_waypoints_topic', '/input_waypoints').value
        self.output_topic = self.declare_parameter('output_path_topic', '/smoothed_path').value
        self.sample_spacing = float(self.declare_parameter('sample_spacing', 0.1).value)
        self.smooth_factor = float(self.declare_parameter('smooth_factor', 0.0).value)

        self.sub = self.create_subscription(Path, self.input_topic, self.path_cb, 10)
        self.pub = self.create_publisher(Path, self.output_topic, 10)

    def path_cb(self, msg: Path):
        if len(msg.poses) < 3:
            self.pub.publish(msg)
            return

        pts = np.array([[p.pose.position.x, p.pose.position.y] for p in msg.poses], dtype=float)
        seg = np.linalg.norm(np.diff(pts, axis=0), axis=1)
        s = np.insert(np.cumsum(seg), 0, 0.0)
        total_len = s[-1]
        if total_len < 1e-6:
            self.pub.publish(msg)
            return

        try:
            tck, _ = splprep([pts[:, 0], pts[:, 1]], u=s, s=self.smooth_factor, k=min(3, len(pts) - 1))
            num_samples = max(3, int(total_len / self.sample_spacing))
            u_new = np.linspace(0.0, total_len, num_samples)
            x_new, y_new = splev(u_new, tck)
        except Exception as exc:
            self.get_logger().warn(f'Spline smoothing failed: {exc}')
            self.pub.publish(msg)
            return

        out = Path()
        out.header = msg.header
        for i in range(len(x_new)):
            ps = PoseStamped()
            ps.header = out.header
            ps.pose.position.x = float(x_new[i])
            ps.pose.position.y = float(y_new[i])
            if i < len(x_new) - 1:
                dx = x_new[i + 1] - x_new[i]
                dy = y_new[i + 1] - y_new[i]
            else:
                dx = x_new[i] - x_new[i - 1]
                dy = y_new[i] - y_new[i - 1]
            yaw = np.arctan2(dy, dx)
            ps.pose.orientation.z = np.sin(yaw / 2.0)
            ps.pose.orientation.w = np.cos(yaw / 2.0)
            out.poses.append(ps)

        self.pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = PathSmootherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
