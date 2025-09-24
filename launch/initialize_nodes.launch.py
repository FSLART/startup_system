from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, TimerAction
import os

def generate_launch_description():
    
    xsens_parameters_file_path = os.path.join(get_package_share_directory('xsens_mti_ros2_driver'), 'param', 'xsens_mti_node.yaml')

    mission_controller_node = Node(
        package='mission_controller',
        executable='mission_controller',
        name='mission_controller',
        output='screen',
        arguments=['--ros-args', '--log-level', 'warn'],
    )

    state_controller_node = Node(
        package='state_controller',
        executable='state_controller',
        name='state_controller',
        output='screen',
        arguments=['--ros-args', '--log-level', 'warn'],
    )

    zed_node = Node(
        package='zed_bridge',
        executable='zed_bridge',
        name='zed_bridge',
        output='screen',
        
    )

    imu_node = Node(
        package='xsens_mti_ros2_driver',  # Correct package name
        executable='xsens_mti_node',
        name='xsens_mti_node',
        output='screen',
        parameters=[xsens_parameters_file_path],  # Use the parameters file
        arguments=[]
    )

    tf_node = Node(
        package="tf2_ros", 
        executable="static_transform_publisher", 
        arguments=["-0.5", "0", "0.95", "0", "0", "0", "base_footprint", "zed_camera_center"]
    )

    ekf_node = Node(
        package='ekf_node',
        executable='ekf_node',
        name='ekf_node',
        output='screen',
        # arguments=['--ros-args', '--log-level', 'warn'],
    )

    # other_nodes = [
    #     #IncludeLaunchDescription(
    #     #    XMLLaunchDescriptionSource([
    #      #       get_package_share_directory('foxglove_bridge'),
    #       #      '/launch/foxglove_bridge_launch.xml'
    #        # ])
    #     #),
    # ]

    return LaunchDescription([
        tf_node,
        mission_controller_node,
        zed_node,
        imu_node,
        ekf_node,

        TimerAction(
            period=1.0,
            actions=[state_controller_node]
        ),        
    ])