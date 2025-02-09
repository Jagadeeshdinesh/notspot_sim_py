#!/usr/bin/env python 
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def perform_trajectory():
    rospy.init_node('open_manipulator_publisher')
    controller_name='/open_manipulator/arm_controller/command'
    trajectory_publisher = rospy.Publisher(controller_name,JointTrajectory, queue_size=10)
    argv = sys.argv[1:]
    arm_joints = ['joint1', 'joint2', 'joint3', 'joint4', 'gripper','gripper_sub']
    goal_positions = [float(argv[0]),float(argv[1]),float(argv[2]),float(argv[3]),float(argv[4]),float(argv[5])]
    rospy.loginfo("Goal Position reached!!!!!!")
    rospy.sleep(1)

    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = arm_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = goal_positions
    trajectory_msg.points[0].velocities = [0.0 for i in arm_joints]
    trajectory_msg.points[0].accelerations = [0.0 for i in arm_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publisher.publish(trajectory_msg)

if __name__ == '__main__':
    perform_trajectory()