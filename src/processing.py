import os, sys, inspect, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import math

class LeapMotionListener(Leap.Listener):
	global_command = ''
	global_section = ''
	stage = 0
	instrumentStageDone = False
	def on_init(self, controller):
		print 'Initialised'
	def on_connect(self, controller):
		print 'Sensor Connected'

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)

		controller.config.set("Gesture.Circle.MinRadius", 15)
		controller.config.set("Gesture.Circle.MinArc", 1)
		controller.config.set("Gesture.Swipe.MinLength", 75.0)
		controller.config.set("Gesture.Swipe.MinVelocity", 75)
		controller.config.set("Gesture.KeyTap.MinDownVelocity", 40.0)
		controller.config.set("Gesture.KeyTap.HistorySeconds", .2)
		controller.config.set("Gesture.KeyTap.MinDistance", 5.0)
		controller.config.save()

		self.instrumentStageDone = False
	def on_disconnect(self, controller):
		print 'Sensor disconnected!'
	def on_exit(self, controller):
		print 'Exited'
	def on_frame(self, controller):
		frame = controller.frame()
		previousFrame = controller.frame(10)


		if self.instrumentStageDone == False:
			self.global_section = self.instrumentStageStart(frame,previousFrame)
			if self.global_section != None:
				print self.global_section
				self.instrumentStageDone = True
		elif self.instrumentStageDone == True:
			self.global_command = self.handStageCommand(frame,previousFrame)
			if self.global_command != None:
				print self.global_command
				self.instrumentStageDone = False

		
	def instrumentStageStart(self, frame, previousFrame):
		if(frame.hands.is_empty == False) and (previousFrame.hands.is_empty):
			all_hands = frame.hands
			if(len(all_hands) == 1):
				hand = all_hands.rightmost
				yaw = self.findYaw(hand)
				if not (hand.fingers.is_empty):
					index_extended = False
					thumb_extended = False
					for finger in hand.fingers:
						if (finger.is_extended == True) and (finger.type == 1):
							index_extended = True
						elif(finger.is_extended == True) and (finger.type == 0):
							thumb_extended = True
					if (index_extended == True) and (thumb_extended == True):
						return 'all sections'
				if -90 <= yaw and yaw <= -60:
					return 'first section'
				elif -60 < yaw and yaw <= -30:
					return 'second section'
				elif -30 < yaw and yaw <= 0:
					return 'third section'
				elif 0 < yaw and yaw <= 30:
					return 'fourth section'
				elif 30 < yaw and yaw <= 60:
					return 'fifth section'
				elif 60 < yaw and yaw <= 90:
					return 'sixth section'

	def handStageCommand(self, frame, previousFrame):
		command = None
		if(frame.hands.is_empty):
			return None
		else:
			all_hands = frame.hands
			if(len(all_hands) == 1):
				if self.checkStab(frame, previousFrame) == True:
					command = 'Stab'
				elif self.checkRaise(frame, previousFrame) != None:
					command = self.checkRaise(frame, previousFrame)
			else:
				right_hand = all_hands.rightmost
				left_hand = all_hands.leftmost

				for gesture in frame.gestures(previousFrame):
					if gesture.state is Leap.Gesture.STATE_STOP:
						if gesture.type is Leap.Gesture.TYPE_SWIPE:
							rightVertical = self.findVertical(right_hand)
							leftVertical = self.findVertical(left_hand)
							average_vertical = 0.5*(rightVertical+leftVertical)
							if 0 <= average_vertical and average_vertical <= 150:
								command = 'heldnotelow'
							elif 150 < average_vertical and average_vertical <=300:
								command = 'heldnotemid'
							elif 300 < average_vertical and average_vertical <= 450:
								command = 'heldnotehigh'
						if gesture.type is Leap.Gesture.TYPE_CIRCLE:
							command = 'minimalism'
						elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
							command = 'pointilism'
				if self.checkImprov(frame, previousFrame) != None:
					command = 'Improvise'
			return command

	def checkStab(self, frame, previousFrame):
		if frame.hands.is_empty:
			return False
		else:
			all_hands_now = frame.hands
			all_hands_start = previousFrame.hands

			if(len(all_hands_now) >= 2) or (len(all_hands_start) >=2):
				return False
			else:
				hand_now = all_hands_now.rightmost
				hand_before = all_hands_start.rightmost
				for finger in hand_now.fingers:
					if finger.is_extended:
						return False
				vertical_now = hand_now.palm_position.y
				vertical_before = hand_before.palm_position.y
				diff = vertical_before - vertical_now
				if diff > 100:
					return True
				else:
					return False

	def checkImprov(self, frame, previousFrame):
		if frame.hands.is_empty:
			return None
		else:
			hands = frame.hands
			if (len(hands) < 2):
				return None
			else:
				right_hand = hands.rightmost
				left_hand = hands.leftmost
				for finger in right_hand.fingers:
					if finger.type is Leap.Finger.TYPE_THUMB:
						if finger.is_extended:
							thumb_pos1 = finger.tip_position
						else:
							return None
					if finger.type is Leap.Finger.TYPE_INDEX:
						if finger.is_extended:
							index_pos1 = finger.tip_position
						else:
							return None
				for finger in left_hand.fingers:
					if finger.type is Leap.Finger.TYPE_THUMB:
						if finger.is_extended:
							thumb_pos2 = finger.tip_position
						else:
							return None
					if finger.type is Leap.Finger.TYPE_INDEX:
						if finger.is_extended:
							index_pos2 = finger.tip_position
						else:
							return None
				if(thumb_pos1.distance_to(thumb_pos2) <= 20 and index_pos1.distance_to(index_pos2) <= 20):
					return 'Improvise'



	def checkRaise(self, frame, previousFrame):
		if frame.hands.is_empty or previousFrame.hands.is_empty:
			return None
		else:
			all_hands_now = frame.hands
			all_hands_start = previousFrame.hands

			if(len(all_hands_now) >= 2) or (len(all_hands_start) >= 2):
				return None
			else:
				hand_now = all_hands_now.rightmost
				hand_before = all_hands_start.rightmost
				vertical_now = self.findVertical(hand_now)
				vertical_before = self.findVertical(hand_before)

				diff = vertical_before - vertical_now
				if diff < -100:
					return 'Raise volume'
				elif diff > 100:
					return 'Lower volume'


	def findVertical(self, hand):
		vertical = hand.palm_position.y
		if vertical >= 600:
			vertical = 600
		return vertical


	def findYaw(self, hand):
		direction = hand.direction
		yaw = math.degrees(direction.yaw)
		if yaw > 90:
			yaw = 90
		if yaw < -90:
			yaw = -90
		return yaw
def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()

	controller.add_listener(listener)

	sys.stdin.readline()
	
if __name__ == "__main__":
	main()

	
