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
    waypoint= [[-1.57, -1.7, 1.3, 1.0, 2.0, 2.0],
               [-1.57, -1.7, 1.3, 0.0, 2.0, 2.0],
               [-1.57, 1.0, 0.0, 0.5, 2.0, 2.0],
               [-1.57, 1.0, 0.0, 0.5, -1.0, -1.0],
               [-1.57, 0.3, 0.0, 0.5, -1.0, -1.0],
               [1.57, 0.0, 0.0, 0.40, -1.0, -1.0],
               [1.57, 0.0, 0.0, 0.9, 1.0, 1.0],
               [1.57, 0.0, 0.0, 0.2, -1.0, -1.0],
               [-1.57, 0.0, 0.0, 0.2, -1.0, -1.0],
               [-1.57, -1.0, 0.8, 1.0, -1.0, -1.0],
               [-1.57, -1.7, 1.3, 1.0, -1.0, -1.0]
               ]

    for j in range (len(waypoint)):
        for i in range(len(command_topics)):
            pub = rospy.Publisher(command_topics[i], Float64, queue_size=10)
            rospy.loginfo(waypoint[j][i])
            pub.publish(waypoint[j][i])
            rate.sleep()
            rospy.sleep(0.2)  
        rospy.sleep(0.3)  

if __name__ == '__main__':
    talker()
    