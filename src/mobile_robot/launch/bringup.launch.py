from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    pkg_share = FindPackageShare("mobile_robot")

    world_file = PathJoinSubstitution([pkg_share, "sdf", "warehouse.sdf"])
    model_path = PathJoinSubstitution([pkg_share, "models"])
    return LaunchDescription([

        SetEnvironmentVariable(
            name="IGN_GAZEBO_RESOURCE_PATH",
            value=[
                model_path,
                ":",
                EnvironmentVariable("IGN_GAZEBO_RESOURCE_PATH", default_value=""),
            ],
        ),

        ExecuteProcess(
            cmd=["ign", "gazebo", world_file, "-r"],
            output="screen"
        ),

        Node(
            package="ros_gz_bridge",
            executable="parameter_bridge",
            arguments=[
                "/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist",
                "/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry",
                "/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan",
                "/tf@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V"
            ],
            output="screen"
        ),
    ])
