import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import math

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
	frame = controller.frame()
	previousFrame = controller.frame(60)

	if(frame.hands.is_empty == False) and (previousFrame.hands.is_empty):
		pass

	elif (frame.hands.is_empty == False):
		all_hands = frame.hands
		if(len(all_hands)<2):
			continue
		right_hand = all_hands.rightmost
		left_hand = all_hands.leftmost

		for gesture in frame.gestures(previousFrame):
			if gesture.type == Leap.Gesture.TYPE_SWIPE:
				command =




class Interface:
	lastFrameID = 0
	frameID = 0

	def processGestures(frame):

	def processFrames(frame, lastFrame):
		if(frame.id == lastFrameID):
			return
		self.lastFrameID = frame.id


