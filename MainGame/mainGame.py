import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('SoundPainting')

pygame.mixer.init(channels = 6)
#1=brass, 2=percussions, 3=piano, 4=strings, 5=voice, 6=woods, 7=all

for x in range (6):
	instrument = x+1
	pygame.mixer.Channel(instrument).set_volume(0.5)

instrument = 0
command = 0

while True:
	while command == 0 or instrument == 0:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quite()
				sys.exit()
				pygame.display.update()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					instrument = 1
					print ("key A pressed")
				if event.key == pygame.K_z:
					instrument = 2
				if event.key == pygame.K_e:
					instrument = 3
				if event.key == pygame.K_r:
					instrument = 4
				if event.key == pygame.K_t:
					instrument = 5
				if event.key == pygame.K_y:
					instrument = 6
				if event.key == pygame.K_u:
					instrument = 7
				if event.key == pygame.K_KP1:
					command = 1
					print ("keypad 1 pressed")
				if event.key == pygame.K_KP2:
					command = 2
				if event.key == pygame.K_KP3:
					command = 3
				if event.key == pygame.K_KP4:
					command = 4
				if event.key == pygame.K_KP5:
					command = 5
				if event.key == pygame.K_KP6:
					command = 6
				if event.key == pygame.K_KP7:
					command = 7
				if event.key == pygame.K_KP8:
					command = 8
				if event.key == pygame.K_KP9:
					command = 9
				if event.key == pygame.K_KP_DIVIDE:
					command = 10
				if event.key == pygame.K_KP_MULTIPLY:
					command = 11
	#while loop waiting for commands

	#Held high
	if command == 1:
		if instrument == 1:
			filePath = "../Audio/Brass/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 2:
			filePath = "../Audio/Percussions/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 3:
			filePath = "../Audio/Piano/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 4:
			filePath = "../Audio/Strings/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 5:
			filePath = "../Audio/Voice/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1) 
		elif instrument == 6:
			filePath = "../Audio/Woods/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/HeldHigh/held_high_" + str(randint(1,3)) + ".wav"
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Held mid
	elif command == 2:
		if instrument == 1:
			filePath = "../Audio/Brass/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 2:
			filePath = "../Audio/Percussions/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 3:
			filePath = "../Audio/Piano/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 4:
			filePath = "../Audio/Strings/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 5:
			filePath = "../Audio/Voice/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 6:
			filePath = "../Audio/Woods/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/HeldMid/held_mid_" + str(randint(1,3)) + ".wav"
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Held low
	elif command == 3:
		if instrument == 1:
			filePath = "../Audio/Brass/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 2:
			filePath = "../Audio/Percussions/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 3:
			filePath = "../Audio/Piano/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 4:
			filePath = "../Audio/Strings/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 5:
			filePath = "../Audio/Voice/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 6:
			filePath = "../Audio/Woods/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/HeldLow/held_low_" + str(randint(1,3)) + ".wav"
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Pointillism
	elif command == 4:
		if instrument == 1:
			filePath = "../Audio/Brass/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 2:
			filePath = "../Audio/Percussions/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 3:
			filePath = "../Audio/Piano/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 4:
			filePath = "../Audio/Strings/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 5:
			filePath = "../Audio/Voice/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 6:
			filePath = "../Audio/Woods/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/Pointillism/pointillism_" + str(randint(1,3)) + ".wav"
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Minimalism
	elif command == 5:
		if instrument == 1:
			filePath = "../Audio/Brass/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 2:
			filePath = "../Audio/Percussions/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 3:
			filePath = "../Audio/Piano/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 4:
			filePath = "../Audio/Strings/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 5:
			filePath = "../Audio/Voice/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 6:
			filePath = "../Audio/Woods/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/Minimalism/minimalism_" + str(randint(1,3)) + ".wav"
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Improv
	elif command == 5:
		if instrument == 1:
			filePath = "../Audio/Brass/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		if instrument == 2:
			filePath = "../Audio/Percussions/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		if instrument == 3:
			filePath = "../Audio/Piano/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		if instrument == 4:
			filePath = "../Audio/Strings/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		if instrument == 5:
			filePath = "../Audio/Voice/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		if instrument == 6:
			filePath = "../Audio/Woods/Improv/improv_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		elif instrument == 7:
			for x in range (6):
				ext=".wav"
				if x == 0:
					name="Brass"
				elif x == 1:
					name="Percussions"
				elif x == 2:
					name ="Piano"
				elif x == 3:
					name = "Strings"
				elif x == 4:
					name = "Voice"
				elif x == 5:
					name = "Woods"
				filePath = "../Audio/" + name + "/Improv/improv_" + str(randint(1,3)) + ext
				soundFile = pygame.mixer.Sound(filePath)
				pygame.mixer.Channel(instrument).play(soundFile, loops = -1)

	#Laugh
	elif command == 6:
		if instrument == 5:
			filePath = "../Audio/Voice/Laughter/laughter_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		else:
			print ("Only the voice section can laugh")

	#Talk
	elif command == 7:
		if instrument == 5:
			filePath = "../Audio/Voice/Talk/talk_" + str(randint(1,3)) + ".wav"
			soundFile = pygame.mixer.Sound(filePath)
			pygame.mixer.Channel(instrument).play(soundFile, loops = -1)
		else:
			print ("Only the voice section can talk")

	#Stop
	elif command == 8:
		if instrument == 1:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 2:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 3:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 4:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 5:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 6:
			pygame.mixer.Channel(instrument).stop()
		elif instrument == 7:
			for x in range (6):
				instrument = x+1
				pygame.mixer.Channel(instrument).stop



	#Vup
	elif command == 9:
		if instrument == 7:
			for x in range (6):
				instrument = x+1
				current = pygame.mixer.Channel(instrument).get_volume()
				new = current - 0.1
				if new < 0:
					new = 0
				if new > 1:
					new = 1
				pygame.mixer.Channel(instrument).set_volume(new)
		else: 
			current = pygame.mixer.Channel(instrument).get_volume()
			pygame.mixer.Channel(instrument).set_volume(current+0.1)

	#Vdown
	elif command == 11:
		if instrument == 7:
			for x in range (6):
				instrument = x+1
				current = pygame.mixer.Channel(instrument).get_volume()
				new = current - 0.1
				if new < 0:
					new = 0
				if new > 1:
					new = 1
				pygame.mixer.Channel(instrument).set_volume(new)
		else: 
			current = pygame.mixer.Channel(instrument).get_volume()
			new = current - 0.1
			if new < 0:
				new = 0
			if new > 1:
				new = 1
			pygame.mixer.Channel(instrument).set_volume(new)

	#Default
	#reset command & instrument to null

	instrument = 0
	command = 0