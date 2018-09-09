#!/usr/bin/env python
import RPi.GPIO as GPIO
import rospy
import std_msgs.msg

GPIO.setmode(GPIO.BOARD)
gpio_list=[15,16,18]
for i in range(3):
    GPIO.setup(gpio_list[i], GPIO.OUT)

def callback(data, id):
  rospy.loginfo("[ID:"+str(id)+"] : " + str(data.data))
  if(data.data==1):
    GPIO.output(gpio_list[id-1],True)
  else:
    GPIO.output(gpio_list[id-1],False)


def listener():
    rospy.init_node('listener', anonymous=True)

    led1 = rospy.Subscriber("/led1", std_msgs.msg.Int8, callback, callback_args=1)
    led2 = rospy.Subscriber("/led2", std_msgs.msg.Int8, callback, callback_args=2)
    led3 = rospy.Subscriber("/led3", std_msgs.msg.Int8, callback, callback_args=3) 
    rospy.spin()

if __name__ == '__main__':
    listener()
