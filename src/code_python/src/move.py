#!/usr/bin/python

import roslib 
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('goforward')
twist = Twist()
twist.linear.x = -0.2 
twist.linear.y = 0.0                                   
pub =rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size = 10)

pub.publish(twist)
rospy.spin() 



