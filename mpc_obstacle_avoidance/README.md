# ROS 2 MPC Trajectory Tracking with LiDAR Obstacle Avoidance

This project replaces pure pursuit with an MPC-based local trajectory tracker, smooths waypoint paths, and supports static and dynamic obstacle avoidance using 2D LiDAR in Gazebo + ROS 2.

## Features
- **Waypoint smoothing** using cubic splines.
- **MPC tracker** for differential-drive robot (`cmd_vel` output).
- **Obstacle-aware local planning** from LiDAR occupancy points.
- **Static and dynamic obstacle handling** by online local detours + automatic return to global path.
- **Dynamic obstacle simulator** that spawns moving objects in front of the robot in Gazebo.

## Package Layout
- `mpc_tracker/path_smoother_node.py`: Converts coarse waypoints to a smooth nav path.
- `mpc_tracker/mpc_tracker_node.py`: MPC tracking + local obstacle detour.
- `mpc_tracker/dynamic_obstacle_spawner.py`: Random dynamic obstacle spawning in Gazebo.
- `config/params.yaml`: Tuning parameters.
- `launch/mpc_navigation.launch.py`: Launches all nodes.

## Dependencies
Install these in your ROS 2 workspace environment:

```bash
sudo apt update
sudo apt install -y ros-$ROS_DISTRO-nav-msgs ros-$ROS_DISTRO-geometry-msgs ros-$ROS_DISTRO-sensor-msgs ros-$ROS_DISTRO-tf2-ros
pip install numpy scipy cvxpy
```

> If `cvxpy` solver is unavailable, install `osqp`: `pip install osqp`

## Integration Steps
1. Copy `mpc_obstacle_avoidance` into your ROS 2 workspace `src` folder.
2. Add a minimal `setup.py`/`package.xml` wrapper if your workspace requires standard colcon packaging.
3. Remap topics in `config/params.yaml` to match your robot:
   - `/odom`
   - `/scan`
   - `/cmd_vel`
4. Publish your original waypoint path to `/input_waypoints` (`nav_msgs/Path`).
5. Launch:

```bash
ros2 launch mpc_obstacle_avoidance mpc_navigation.launch.py
```

## Runtime Behavior
1. Smoother node turns sparse waypoints into dense spline trajectory (`/smoothed_path`).
2. MPC node tracks the trajectory with horizon optimization.
3. When LiDAR detects obstacle in projected corridor, node generates a local offset trajectory around obstacle and continues tracking.
4. After obstacle clears, controller converges back to original smoothed path.

## Tuning Notes
- Increase `safety_radius` for wider clearance.
- Increase `lateral_shift_max` for stronger detour around large obstacles.
- Increase `horizon` for smoother, farther-look planning; reduce for responsiveness.
- Increase `dynamic_obstacle_lookahead` to react earlier to moving obstacles.

## Assignment Mapping
1. ✅ Pure pursuit replaced by MPC tracker.
2. ✅ Waypoints smoothed before control.
3. ✅ Obstacle maneuvering using 2D LiDAR.
4. ✅ Handles static + dynamic obstacles online.
