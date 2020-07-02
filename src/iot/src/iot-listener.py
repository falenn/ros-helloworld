#!/usr/bin/env python
import rospy 
from std_msgs.msg import String
from iot.msg import IoTSensor

def callback(message):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.id)

def listener():
    rospy.init_node('iotlistener', anonymous=True)
    rospy.Subscriber('/iotsensor/status', IoTSensor, callback)
    
    # listen forever
    rospy.spin()

if __name__ == '__main__':
    listener()
