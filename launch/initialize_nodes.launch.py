from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, TimerAction
import os

def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory('safety_monitor'),
        'config',
        'default_params.yaml'
    )

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

    other_nodes = [
        Node(
            package='zed_bridge',
            executable='zed_bridge',
            name='zed_bridge',
            output='screen'
        ),
        #IncludeLaunchDescription(
        #    XMLLaunchDescriptionSource([
         #       get_package_share_directory('foxglove_bridge'),
          #      '/launch/foxglove_bridge_launch.xml'
           # ])
        #),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='rear_axle_link',
            arguments=['-1.5', '0', '-0.3', '0', '0', '0', 'base_footprint', 'rear_axle_link'],
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='zed_camera_center',
            arguments=['-0.85', '0', '0.4', '0', '0', '0', 'base_footprint', 'zed_camera_center'],
            output='screen'
        ),
        Node(
            package='safety_monitor',
            executable='monitor_node',
            name='SafetyMonitorNode',
            parameters=[config_file],
            output='screen'
        ),
    ]

    return LaunchDescription([
        mission_controller_node,

        TimerAction(
            period=1.0,
            actions=[state_controller_node]
        ),

        TimerAction(
            period=2.0,
            actions=other_nodes
        )
    ])