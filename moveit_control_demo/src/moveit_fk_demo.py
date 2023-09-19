#!/usr/bin/env python
#coding:utf-8
import rospy
import sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('moveit_fk_demo', anonymous=True)
        arm = moveit_commander.MoveGroupCommander('arm')
        gripper = moveit_commander.MoveGroupCommander('gripper')
        arm.set_goal_orientation_tolerance(0.01)
        gripper.set_goal_joint_tolerance(0.001)
        arm.set_named_target('right_up')
        arm.go()
        rospy.sleep(2)
        print arm.get_joint_value_target()
        #arm.set_named_target('resting')
        #arm.go()
        #rospy.sleep(1)
        gripper.set_joint_value_target([0.04])
        gripper.go()
        rospy.sleep(1)
        #[-0.0, -2.0, 2.3, 1.4, 0.0]
        joint_positions = [-0.0, -2.0, 2.3, 1.4, 0.0]
        arm.set_joint_value_target(joint_positions)

        arm.go()
        rospy.sleep(5)
        print arm.get_joint_value_target()
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
    