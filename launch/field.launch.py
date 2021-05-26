# Copyright 2021 ShotaAk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import LogInfo
from launch.actions import OpaqueFunction
from launch.actions import SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    declare_arg_world = DeclareLaunchArgument(
        'world', default_value='field01',
        description=('Set an world file name: '
                     '[field01, field02, field03, ..etc]'))

    declare_arg_gui = DeclareLaunchArgument(
        'gui',
        default_value='true',
        description='Set to "false" to run headless.')

    declare_arg_server = DeclareLaunchArgument(
        'server',
        default_value='true',
        description='Set to "false" not to run gzserver.')

    def func_world_file_name(context):
        world_file = os.path.join(
            get_package_share_directory('hac_gazebo'),
            'worlds',
            context.launch_configurations['world'] + '.world')

        if os.path.exists(world_file):
            return [SetLaunchConfiguration('world_file_name', world_file)]
        else:
            return [LogInfo(msg=world_file + " is not exist.")]
    get_world_file_name = OpaqueFunction(function=func_world_file_name)

    gzserver = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                get_package_share_directory('gazebo_ros'),
                '/launch/gzserver.launch.py']),
            condition=IfCondition(LaunchConfiguration('server')),
            launch_arguments={'world': LaunchConfiguration('world_file_name')}.items(),
        )

    gzclient = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                get_package_share_directory('gazebo_ros'),
                '/launch/gzclient.launch.py']),
            condition=IfCondition(LaunchConfiguration('gui'))
        )

    # spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
    #                     arguments=['-entity', 'crane_plus', '-x', '0', '-y', '0',
    #                                '-z', '1.02', '-topic', '/robot_description'],
    #                     output='screen')

    return LaunchDescription([
        declare_arg_world,
        declare_arg_gui,
        declare_arg_server,
        get_world_file_name,
        gzserver,
        gzclient,
    ])