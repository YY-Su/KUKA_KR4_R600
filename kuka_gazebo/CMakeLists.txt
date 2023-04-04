cmake_minimum_required(VERSION 3.0.2)
project(kuka_gazebo)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  controller_manager
  effort_controllers
  gazebo_ros
  gazebo_ros_control
  joint_state_controller
  joint_trajectory_controller
  robot_state_publisher
  moveit_kinematics
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)