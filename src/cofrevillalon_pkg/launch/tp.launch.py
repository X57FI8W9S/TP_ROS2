import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo

def generate_launch_description():
    # Define the path to your RViz configuration file
    rviz_config_file = '/root/ros2_ws/src/cofrevillalon_pkg/config/config1.rviz'

    # Get the launch directory for logging purposes
    launch_dir = os.path.join(get_package_share_directory('cofrevillalon_pkg'), 'launch')

    return LaunchDescription([
        # Action to play the rosbag at half speed
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', 'r2b_galileo2', '-r0.5'],
            output='screen'
        ),

        # Action to launch RViz2 with the specified configuration
        ExecuteProcess(
            cmd=['ros2', 'run', 'rviz2', 'rviz2', '-d', rviz_config_file],
            output='screen'
        ),

        # Log a message indicating which launch file is being used
        LogInfo(msg=f"Running launch file from: {launch_dir}"),
    ])
