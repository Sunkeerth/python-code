from setuptools import setup, find_packages
from glob import glob

package_name = 'mpc_obstacle_avoidance'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='MPC trajectory tracking with lidar obstacle avoidance',
    license='MIT',
    entry_points={
        'console_scripts': [
            'path_smoother_node = mpc_tracker.path_smoother_node:main',
            'mpc_tracker_node = mpc_tracker.mpc_tracker_node:main',
            'dynamic_obstacle_spawner = mpc_tracker.dynamic_obstacle_spawner:main',
        ],
    },
)
