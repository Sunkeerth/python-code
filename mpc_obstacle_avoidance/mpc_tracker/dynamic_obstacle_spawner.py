#!/usr/bin/env python3
import math
import random
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from gazebo_msgs.srv import SpawnEntity, DeleteEntity

CYLINDER_SDF = """
<sdf version='1.6'>
  <model name='{name}'>
    <static>false</static>
    <link name='link'>
      <inertial><mass>0.5</mass></inertial>
      <collision name='collision'>
        <geometry><cylinder><radius>0.18</radius><length>0.6</length></cylinder></geometry>
      </collision>
      <visual name='visual'>
        <geometry><cylinder><radius>0.18</radius><length>0.6</length></cylinder></geometry>
        <material><ambient>0.8 0.1 0.1 1</ambient></material>
      </visual>
    </link>
  </model>
</sdf>
"""


class DynamicObstacleSpawner(Node):
    def __init__(self):
        super().__init__('dynamic_obstacle_spawner')
        p = self.declare_parameter
        self.enabled = bool(p('enabled', True).value)
        self.odom_topic = p('robot_odom_topic', '/odom').value
        self.spawn_interval = float(p('spawn_interval_sec', 7.0).value)
        self.lifetime = float(p('obstacle_lifetime_sec', 14.0).value)
        self.dmin = float(p('spawn_distance_min', 1.2).value)
        self.dmax = float(p('spawn_distance_max', 3.0).value)
        self.lat = float(p('lateral_range', 0.8).value)

        self.spawn_cli = self.create_client(SpawnEntity, '/spawn_entity')
        self.delete_cli = self.create_client(DeleteEntity, '/delete_entity')
        self.sub = self.create_subscription(Odometry, self.odom_topic, self.odom_cb, 10)
        self.timer = self.create_timer(self.spawn_interval, self.tick)
        self.cleanup_timer = self.create_timer(1.0, self.cleanup)

        self.robot = None
        self.spawned = {}
        self.counter = 0

    def odom_cb(self, msg):
        p = msg.pose.pose.position
        q = msg.pose.pose.orientation
        yaw = math.atan2(2.0 * (q.w * q.z), 1.0 - 2.0 * (q.z * q.z))
        self.robot = (p.x, p.y, yaw)

    def tick(self):
        if not self.enabled or self.robot is None or not self.spawn_cli.service_is_ready():
            return
        rx, ry, ryaw = self.robot
        d = random.uniform(self.dmin, self.dmax)
        lat = random.uniform(-self.lat, self.lat)
        x = rx + d * math.cos(ryaw) - lat * math.sin(ryaw)
        y = ry + d * math.sin(ryaw) + lat * math.cos(ryaw)

        name = f'dyn_obs_{self.counter}'
        self.counter += 1

        req = SpawnEntity.Request()
        req.name = name
        req.xml = CYLINDER_SDF.format(name=name)
        req.robot_namespace = ''
        req.initial_pose.position.x = float(x)
        req.initial_pose.position.y = float(y)
        req.initial_pose.position.z = 0.3

        self.spawn_cli.call_async(req)
        self.spawned[name] = self.get_clock().now().nanoseconds / 1e9

    def cleanup(self):
        if not self.delete_cli.service_is_ready():
            return
        now = self.get_clock().now().nanoseconds / 1e9
        for name, t0 in list(self.spawned.items()):
            if now - t0 > self.lifetime:
                req = DeleteEntity.Request()
                req.name = name
                self.delete_cli.call_async(req)
                del self.spawned[name]


def main(args=None):
    rclpy.init(args=args)
    node = DynamicObstacleSpawner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
