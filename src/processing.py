import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import math

def stageStart(frame, previousFrame):
	if(frame.hands.is_empty == False) and (previousFrame.hands.is_empty):
		all_hands = frame.hands
		if(len(all_hands) == 1):
			hand = all_hands.rightmost
			yaw = findYaw(hand)
			if not (hand.fingers.is_empty):
				index_extended = False
				thumb_extended = False
				for finger in hand.fingers:
					if (finger.is_extended == True) and (finger.type == Finger.TYPE_INDEX):
						index_extended = True
					elif(finger.is_extended == True) and (finger.type == Finger.TYPE_THUMB):
						thumb_extended = True
				if (index_extended == True) and (thumb_extended == True):
					return 'all sections'
			if x < yaw and yaw < y:
				return 'first section'
			elif x1 < yaw and yaw < y1:
				return 'second section'
			elif x2 < yaw and yaw < y2:
				return 'third section'
			elif x3 < yaw and yaw < y3:
				return 'fourth section'
			elif x4 < yaw and yaw < y4:
				return 'fifth section'
			elif x5 < yaw and yaw < y5:
				return 'sixth section'

def stageCommand(frame, previousFrame):
	if(frame.hands.is_empty == False) and (previousFrame.hands.is_empty):
		return None
	else:
		all_hands = frame.hands
		if(len(all_hands) < 2):
			return None
		else:
			right_hand = all_hands.rightmost
			left_hand = all_hands.leftmost

			for gesture in frame.gestures(previousFrame):
				if gesture.state is Gesture.STATE_STOP:
					if gesture.type is Leap.Gesture.TYPE_SWIPE:
						rightVertical = findVertical(right_hand)
						leftVertical = findVertical(left_hand)
						average_vertical = 0.5*(rightVertical+leftVertical)
						if x < average_vertical and average_vertical < y:
							command = 'heldnotelow'
						elif x1 < average_vertical and average_vertical <y1:
							command = 'heldnotemid'
						elif x2 < average_vertical and average_vertical < y2:
							command = 'heldnotehigh'

					elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
						command = 'pointilism'
					elif gesture.type == Leap.Gesture.TYPE_CIRCLE:
						command = 'command1'
			if checkStab(frame, previousFrame) == True:
				command = 'Stab'
			elif checkMinimal(frame, previousFrame) == True:
				command = 'minimalism'
			elif checkFish(frame, previousFrame) == True:
				command = 'Fish'
			elif checkImprov(frame, previousFrame) == True:
				command = 'Improvise'
			elif checkAirSounds(frame, previousFrame) == True:
				command = 'Air Souncs'
			elif checkWhistle(frame, previousFrame) == True:
				command = 'Whistle'
			elif checkAnnuler(frame, previousFrame) == True:
				command = 'Stop all'
			elif checkRaise(frame, previousFrame) == True:
				command = 'Raise/Decrease volume'
			elif checkSpeed(frame, previousFrame) == True:
				command = 'Raise/Decrease tempo'

def checkStab(frame, previousFrame):
def checkFish(frame, previousFrame):
def checkImprov(frame, previousFrame):
def checkAirSounds(frame, previousFrame):
def checkWhistle(frame, previousFrame):
def checkAnnuler(frame, previousFrame):
def checkRaise(frame, previousFrame):
def checkSpeed(frame, previousFrame):

def findVertical(hand):
	vertical = hand.palm_position.y
	if vertical >= 600:
		vertical = 600
	return vertical

def findPitch(hand):

def findRoll(hand):

def findYaw(hand):

STAGE_START = 0
STAGE_COMMAND = 1
STAGE_SEND = 2

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
stage = STAGE_START
while True:
	previousFrame = controller.frame(60)
	frame = controller.frame()
	
