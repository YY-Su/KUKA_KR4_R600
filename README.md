# KUKA-KR4-R600
Project for school work utilizing the KUKA_KR4_R600 robotic arm.

Set-up instructions for RSI can be found here:
* kuka_rsi_hw_interface/include/kuka_rsi_hw_interface/KRC4 
* kuka_rsi_hw_interface/include/kuka_rsi_hw_interface/KRC2

## Features:
* Utilizing ROS + RSI(Robotic_Sensor_Interface)
* Basic Point to Point motion

## Instructions to move robot

1: roslaunch kuka_rsi_hw_interface test_hardware_interface.launch

2: roslaunch kuka_kr4_moveit moveit_controller.launch<br>--This step will luanch moveit GUI and you can move the robot already--

3: rosrun kuka_kr4_bringup simple_movement.py<br>--This will run the 4 coordinate movement, edit it for diff postition--
echo # KUKA_KR4_R600


![](https://github.com/YY-Su/KUKA_KR4_R600/blob/main/kuka.gif)

## Reference: 
Majority of packages were taken from KUKA_EXPERIMENTAL  
* https://github.com/ros-industrial/kuka_experimental
