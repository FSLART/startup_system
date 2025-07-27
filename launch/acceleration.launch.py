import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory('safety_monitor'),
        'config',
        'default_params.yaml'
    )

    spac_config_file = os.path.join(
        get_package_share_directory('spac2_0'),
        'config',
        'demo_params.yaml'
    )

    return LaunchDescription([
        # Node(
        #     package='safety_monitor',
        #     executable='monitor_node',
        #     name='SafetyMonitorNode',
        #     parameters=[config_file],
        #     output='screen'
        # ),
        # Node(
        #    package='zed_bridge',
        #    executable='zed_bridge',
        #    name='zed_bridge',
        #    output='screen',
        # ),
        # Node(
        #     package='ekf_node',
        #     executable='ekf_node',
        #     name='ekf_node',
        #     output='screen',
        # ),
        Node(
            package='spac2_0',
            executable='spac_node',
            name='spac_node',
            parameters=[spac_config_file],
            output='screen',
        ),
        Node(
            package='path_planner',
            executable='my_node',
            name='path_planner',
            arguments=['--ros-args', '-p', 'planner_mode:=4'],
        ),
        # Node(
        #     package="tf2_ros", 
        #     executable="static_transform_publisher", 
        #     arguments=["-0.5", "0", "0.95", "0", "0", "0", "base_footprint", "zed_camera_center"]
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='rear_axle_link',
        #     arguments=['-1.5', '0', '-0.3', '0', '0', '0', 'base_footprint', 'rear_axle_link'],
        #     output='screen'
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='zed_camera_center',
        #     arguments=['-0.85', '0', '0.4', '0', '0', '0', 'base_footprint', 'zed_camera_center'],
        #     output='screen'
        # ),
        
    ])
