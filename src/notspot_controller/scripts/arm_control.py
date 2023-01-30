#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64 , Float64MultiArray
import math

def talker():
    rospy.init_node('arm_commander', anonymous=True)
    command_topics = ["/notspot_controller/joint1/command",
                  "/notspot_controller/joint2/command",
                  "/notspot_controller/joint3/command",
                  "/notspot_controller/joint4/command",
                  "/notspot_controller/joint5/command",
                  "/notspot_controller/joint6/command"]
    
    rate = rospy.Rate(5) # 10hz

    position = [-1.57, -1.7, 1.3, 1.0, 2.0, 2.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
        rospy.sleep(0.4)  

    position = [-1.57, -1.7, 1.3, 0.0, 2.0, 2.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [-1.57, 1.0, 0.0, 0.5, 01.0, 01.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4)  

    position = [-1.57, 1.0, 0.0, 0.5, -1.0, -1.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4)  

    position = [-1.57, 1.0, 0.0, 0.0, -1.0, -1.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [-1.57, 1.0, -1.0, 0.0, -1.0, -1.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [1.57, 0.3, 0.0, 0.0, -1.0, -1.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [1.57, 0.3, 0.0, 0.90, -1.0, -1.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [1.57, 0.3, 0.0, 0.90, 0.0, 0.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [1.57, 0.0, 0.0, 0.90, 0.0, 0.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
    rospy.sleep(0.4) 

    position = [-1.57, -1.7, 1.3, 1.0, 2.0, 2.0]
    for i in range(len(command_topics)):
        pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
        rospy.loginfo(position[i])
        pub.publish(position[i])
        rate.sleep()
        rospy.sleep(0.4)

if __name__ == '__main__':
    talker()
    # try:
    #     talker()
    # except rospy.ROSInterruptException:
    #     pass