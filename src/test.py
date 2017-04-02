#this is the test suite to analyse readings from the leap motion sensor
#so that I can implement limits, and accurate readings to avoid destabilisation
#of the drone in-flight.

import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import math

#common initial reading of the hand's position on top of the leap motion sensor
storedPitch = -1.503539253670133
storedYaw = -14.89836891011053
storedRoll = 26.59556988266136
storedVertical =150

pitch = storedPitch
yaw =storedYaw
roll =storedRoll
vertical =storedVertical

#activates the controller and enables gestures
controller = Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
controller.config.set("Gesture.Swipe.MinLength", 30.0)
controller.config.set("Gesture.Swipe.MinVelocity", 150)
controller.config.save()
righthand1 = 0

while True:
  #previousFrame = controller.frame()
  #time.sleep(0.05)
  frame = controller.frame()
  all_hands = frame.hands
  righthand = all_hands.rightmost
          
  pointables = righthand.pointables
  fingers = righthand.fingers

  index_finger_list1 = righthand.fingers.finger_type(1)
  index_finger1 = index_finger_list1[0]

  tip1 = index_finger1.tip_position

  lefthand = all_hands.leftmost
  pointables = lefthand.pointables
  fingers = lefthand.fingers

  index_finger_list2 = lefthand.fingers.finger_type(1)
  index_finger2 = index_finger_list2[0]

  tip2 = index_finger2.tip_position

  thumb_list1 = righthand.fingers.finger_type(0)
  thumb_1 = thumb_list1[0]

  tipThumb1 = thumb_1.tip_position

  thumb_list2 = lefthand.fingers.finger_type(0)
  thumb_2 = thumb_list2[0]

  tipThumb2 = thumb_2.tip_position
  if(tip1.x > 0 or tip1.y > 0 or tip1.z > 0 and tip2.x > 0 or tip2.y > 0 or tip2.z > 0 and tipThumb1.x > 0 or tipThumb1.y > 0 or tipThumb1.z > 0 and tipThumb2.x > 0 or tipThumb2.y > 0 or tipThumb2.z > 0):
    if(tip1.distance_to(tip2) <= 10 and tipThumb1.distance_to(tipThumb2) <= 10):
      print "Meeting"

  print tip1 ,",", tip2
  time.sleep(2)     


