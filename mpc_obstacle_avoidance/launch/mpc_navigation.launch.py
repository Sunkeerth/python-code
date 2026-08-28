from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('mpc_obstacle_avoidance')
    params = os.path.join(pkg_share, 'config', 'params.yaml')

    return LaunchDescription([
        Node(
            package='mpc_obstacle_avoidance',
            executable='path_smoother_node',
            name='path_smoother_node',
            parameters=[params],
            output='screen',
        ),
        Node(
            package='mpc_obstacle_avoidance',
            executable='mpc_tracker_node',
            name='mpc_tracker_node',
            parameters=[params],
            output='screen',
        ),
        Node(
            package='mpc_obstacle_avoidance',
            executable='dynamic_obstacle_spawner',
            name='dynamic_obstacle_spawner',
            parameters=[params],
            output='screen',
        ),
    ])
