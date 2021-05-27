# Humanoid Autonomous Challenge Gazebo

[Humanoid Autonomous Challenge](https://docs.google.com/presentation/d/1vuwCjDXx6wnafV10Z6lkyb3-dfEbjgk4IX_BUWnp6jI/edit?usp=sharing)
のGazeboモデルパッケージです。

## Requirements

- ROS 2 Foxy
- gazebo_ros_pkgs

## Installation

```sh
$ cd ~/ros2_ws/src
$ git clone https://github.com/ShotaAk/hac_gazebo.git
$ rosdep install -r -y -i --from-paths .

$ cd ~/ros2_ws
$ colcon build --symlink-install

$ source ~/ros2_ws/install/setup.bash
```

## Usage

### Field

`field.launch.py`はHACの競技フィールドを起動します。

用意しているフィールドの一覧は[/worlds](./worlds/README.md)を参照してください。

```sh
$ ros2 launch hac_gazebo field.launch.py

# field02.worldを読み込む
$ ros2 launch hac_gazebo field.launch.py world:=field02
```

### Challenge

`challenge**.launch.py`はHACのボールが置かれた競技フィールドを起動します。

用意しているフィールドの一覧は[/launch](./launch/README.md)を参照してください。

```sh
$ ros2 launch hac_gazebo challenge01.launch.py

$ ros2 launch hac_gazebo challenge02.launch.py
```
