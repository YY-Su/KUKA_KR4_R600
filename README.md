# KUKA-KR4-R600
Project for school work utilizing the KUKA_KR4_R600 robotic arm.

## Features:
1. Utilizing ROS + RSI(Robotic_Sensor_Interface)
2. Basic Point to Point motion

## Instructions to move robot

1: roslaunch kuka_rsi_hw_interface test_hardware_interface.launch

2: roslaunch kuka_kr4_moveit moveit_controller.launch<br>--This step will luanch moveit GUI and you can move the robot already--

3: rosrun kuka_kr4_bringup simple_movement.py<br>--This will run the 4 coordinate movement, edit it for diff postition--
echo # KUKA_KR4_R600


## Credits: 
Majority of packages were forked from KUKA_EXPERIMENTAL
https://github.com/ros-industrial/kuka_experimental
