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
	previousFrame = controller.frame()
	time.sleep(0.2)
	frame = controller.frame()
	if frame.hands.is_empty:
		continue
	else:
		hands = frame.hands
		if (len(hands) < 2):
			continue
		else:
			right_hand = hands.rightmost
			left_hand = hands.leftmost
			for finger in right_hand.fingers:
				if finger.type == 0:
					if finger.is_extended:
						thumb_pos1 = finger.tip_position
						print thumb_pos1
					else:
						pass
				elif finger.type == 1:
					if finger.is_extended:
						index_pos1 = finger.tip_position
						print index_pos1
					else:
						pass
			for finger in left_hand.fingers:
				if finger.type == 0:
					if finger.is_extended:
						thumb_pos2 = finger.tip_position
						print thumb_pos2
					else:
						pass
				elif finger.type == 1:
					if finger.is_extended:
						index_pos2 = finger.tip_position
						print index_pos2
					else:
						pass
			if(thumb_pos1.distance_to(thumb_pos2) <= 20 and index_pos1.distance_to(index_pos2) <= 20):
				print 'Improvise'
