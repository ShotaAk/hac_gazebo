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
from launch.actions import IncludeLaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    field = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                get_package_share_directory('hac_gazebo'),
                '/launch/field.launch.py']),
            launch_arguments={'world' : 'field01'}.items()
        )

    spawn_ball1 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'ball1',
                                   '-x', '1.35', '-y', '0.35', '-z', '0.1',
                                   '-database', 'hac_orange_ball'],
                        output='screen')

    spawn_ball2 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'ball2',
                                   '-x', '2.9', '-y', '-0.3', '-z', '0.1',
                                   '-database', 'hac_orange_ball'],
                        output='screen')

    spawn_table1 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'table1',
                                   '-x', '4.65', '-y', '0', '-z', '0.0351',
                                   '-database', 'hac_ball_table_30cm'],
                        output='screen')

    spawn_ball3 = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-entity', 'ball3',
                                   '-x', '4.65', '-y', '0', '-z', '0.4',
                                   '-database', 'hac_orange_ball'],
                        output='screen')

    return LaunchDescription([
        field,
        spawn_ball1,
        spawn_ball2,
        spawn_table1,
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=spawn_table1,
                on_exit=[spawn_ball3]
            )
        ),
    ])