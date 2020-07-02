#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
z=0
yaw=0

def poseCallback(pose_msg):
    rospy.loginfo("callback to update distance")
    global x, y, z, yaw
    x=pose_msg.x
    y=pose_msg.y
    yaw=pose_msg.theta

def move(speed, distance):
    #declare a Twist message and send velocity commands
    vel_msg = Twist()

    # get current location
    x0=x
    y0=y
    #z0=z
    #yaw0=yaw

    # task 1: assign the x coord of linear velocity to speed
    vel_msg.linear.x = speed

    distance_moved = 0.0
    loop_rate = rospy.Rate(10) # publish a msg every 10Hz / 10 times a sec

    # task 2: create a publisher for the velocity msg
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    while True:
        rospy.loginfo("Turtlesim moves foward")
        vel_publisher.publish(vel_msg)
        loop_rate.sleep()

        #measure distnace moved
        distance_moved = distance_moved+abs(0.5*math.sqrt((x-x0)**2 + ((y-y0) ** 2)))
        print "distance moved: %d" % distance_moved

        if not (distance_moved < distance):
            rospy.loginfo("reached")
            vel_msg.linear.x=0
            vel_publisher.publish(vel_msg)
            break

        #task 4: publish a velocity msg zero to make robot stop after dist reached
        
if __name__ == "__main__":
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
        #task 5: declare vel publisher


        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        
        while True:
            time.sleep(2)
            print 'move:'
            move(1.0, 10.0)
            print 'start reset:'
            rospy.wait_for_service('reset')
            reset_turtle = rospy.ServiceProxy('reset', Empty)
            reset_turtle()
            print 'end reset:'

        
    except rospy.ROSInterruptException:
        rospy.loginfo('node terminated')


