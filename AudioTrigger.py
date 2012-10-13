import pygame

from Entity import *

import Colors

class AudioTrigger(Entity):
	def __init__(self, kernel, level, audioFile):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True

		self.mSound = self.mKernel.SoundManager().LoadSound(audioFile)

	def Trigger(self, other):
		self.mSound.play()

		return

	def Draw(self):
		Entity.Draw(self)

		return