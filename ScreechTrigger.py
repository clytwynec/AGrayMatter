import pygame
from pygame.locals import *

from Entity import *

import Colors

class ScreechTrigger(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 60, 45)
		self.mPlayed = False
		self.mSound = self.mKernel.SoundManager().LoadSound("CarScreech.wav")


	def OnCollision(self, other):
		if (other.IsA("Player")):
			if(not self.mPlayed):
				self.mSound.play()
				self.mPlayed = True


	def Draw(self):
		Entity.Draw(self)