#! /usr/bin/env python
    #90 = 1.57
    #120 = 2.44
    #140 = 2.09
    #180 = 3.14
import rospy
import sys
from math import pi, tau, dist, fabs, cos
import moveit_commander

def go_to_joint_state(A1, A2, A3, A4, A5, A6):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("simple_movement", anonymous=True)
        move_group = moveit_commander.MoveGroupCommander("kuka_arm")

        joint_goal = move_group.get_current_joint_values()
        joint_goal[0] = A1
        joint_goal[1] = A2
        joint_goal[2] = A3
        joint_goal[3] = A4
        joint_goal[4] = A5
        joint_goal[5] = A6
        # joint_goal[6] = 0

        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()

if __name__ == '__main__':
    go_to_joint_state(-pi/2, -pi/4, tau/3, 0, -pi*4/9, pi*5/180)
    go_to_joint_state(0, -pi/2, tau*5/12, 0, -pi*4/9, pi*5/180)
    go_to_joint_state(pi/2, -pi/4, tau/3, 0, -pi*4/9, pi*5/180)
    go_to_joint_state(0, -pi*7/9, tau/3, 0, 0 , pi*5/180)
