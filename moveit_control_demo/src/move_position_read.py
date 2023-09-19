#!/usr/bin/env python
#coding:utf-8

import rospy
import sys
import moveit_commander
from control_msgs.msg import GripperCommand

def ros_init():
    rospy.init_node('get_get_joint_value', anonymous=True)
    arm = moveit_commander.MoveGroupCommander('arm')
    gripper = moveit_commander.MoveGroupCommander('gripper')
    while not rospy.is_shutdown():
        print arm.get_current_joint_values() , gripper.get_current_joint_values()
        #rospy.sleep(0.5)


if __name__ == "__main__":
    ros_init()
