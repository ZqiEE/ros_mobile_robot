# Autonomous Warehouse Mobile Robot

A mobile robot platform designed for warehouse material transportation.

The project involved designing the robot chassis in CAD and creating a ROS-based simulation environment to test its model and movement in Gazebo.

## CAD Model

![CAD Demonstration](https://github.com/user-attachments/assets/9aaa192c-b5b0-4a89-9899-9fc4c7f0d1cf)

## RViz Visualization

![RViz](https://github.com/user-attachments/assets/b8d962d6-9998-48b7-9a4c-24d52cc6fde0)

## Gazebo Simulation

https://github.com/user-attachments/assets/2b4dcd47-6df9-49f5-b0e4-da17d5f3a11e

## Run the ROS 2 simulation

This checkout uses the ROS 2 `ros_gz_bridge` with the Ignition Gazebo CLI and
plugin names (the ROS 2 Humble / Gazebo Fortress combination). Install those
packages, then build and launch from the repository root:

```bash
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
ros2 launch mobile_robot bringup.launch.py
```

The package installs the robot as `models/finalassembly_v3`. The launch file
adds the parent `models` directory to `IGN_GAZEBO_RESOURCE_PATH`, and the world
resolves `model://finalassembly_v3` through `model.config`. It no longer
depends on an absolute path from the original developer machine.

The command and feedback boundary is:

- ROS `/cmd_vel` (`geometry_msgs/msg/Twist`) -> `ros_gz_bridge` -> Gazebo
  DiffDrive;
- Gazebo `/odom` -> `ros_gz_bridge` -> ROS `nav_msgs/msg/Odometry`;
- Gazebo `/scan` -> `ros_gz_bridge` -> ROS `sensor_msgs/msg/LaserScan`.

Publishing `/cmd_vel` moves only this simulated model. This repository does
not include a physical motor controller, a hardware safety layer, or evidence
that the same configuration is suitable for a real robot.
