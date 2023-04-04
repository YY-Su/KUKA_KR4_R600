# KUKA-KR4-R600
Project used for school work

## Instruction to move robot

1: roslaunch kuka_rsi_hw_interface test_hardware_interface.launch

2: roslaunch kuka_kr4_moveit moveit_controller.launch<br>--This step will luanch moveit GUI and you can move the robot already--

3: rosrun kuka_kr4_bringup simple_movement.py<br>--This will run the 4 coordinate movement, edit it for diff postition--
echo # KUKA_KR4_R600
