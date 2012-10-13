import pygame

from MaskedLevel import *
import Colors

from pygame.locals import *

class AudioLevel(MaskedLevel):
	def __init__(self, kernel):
		MaskedLevel.__init__(self, kernel)
		
		self.mAudioTriggers = []
		self.mCurrentPlatform = None

	def Load(self, levelName):
		MaskedLevel.Load(self, levelName)

		self.ResetTriggers()

	def ResetTriggers(self):
		for entity in self.mEntities:
			if (entity.IsA("AudioLevelTrigger")):
				self.mAudioTriggers.append(entity)
		
		prev = None
		for trigger in self.mAudioTriggers:
			if not prev:
				prev = trigger
				self.mCurrentPlatform = prev
				self.mCurrentPlatform.Trigger(None)
				continue
			else:
				prev.mNextNode = trigger
				prev = trigger

	def Update(self, delta):
		MaskedLevel.Update(self, delta)