import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import math

controller = Leap.Controller()

controller = Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)

controller.config.set("Gesture.Circle.MinRadius", 10.0)
controller.config.set("Gesture.Circle.MinArc", .5)
controller.config.set("Gesture.Swipe.MinLength", 200.0)
controller.config.set("Gesture.Swipe.MinVelocity", 750)
controller.config.set("Gesture.KeyTap.MinDownVelocity", 40.0)
controller.config.set("Gesture.KeyTap.HistorySeconds", .2)
controller.config.set("Gesture.KeyTap.MinDistance", 1.0)
controller.config.set("Gesture.ScreenTap.MinForwardVelocity", 30.0)
controller.config.set("Gesture.ScreenTap.HistorySeconds", .5)
controller.config.set("Gesture.ScreenTap.MinDistance", 1.0)
controller.config.save()


righthandID = 0
lefthandID = 0
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

  thumb_list1 = righthand.fingers.finger_type(1)
  thumb_1 = thumb_list1[0]

  tipThumb1 = thumb_1.tip_position

  thumb_list2 = lefthand.fingers.finger_type(1)
  thumb_2 = thumb_list2[0]

  tipThumb2 = thumb_2.tip_position

  if(tip1 == tip2 and tipThumb1 == tipThumb2)
    print "Meeting"


  '''
  if frame.hands.is_empty or previousFrame.hands.is_empty:
    continue
  else:
    all_hands_now = frame.hands
    all_hands_start = previousFrame.hands

    if(len(all_hands_now) >= 2) or (len(all_hands_start) >=2):
      continue
    else:
      hand_now = all_hands_now.rightmost
      hand_before = all_hands_start.rightmost

      vertical_now = hand_now.palm_position.y
      vertical_before = hand_before.palm_position.y
      diff = vertical_before - vertical_now
      if diff > 100:
        print 'shit'
  '''       
    
      
			