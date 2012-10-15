import pygame

from Entity import *

import Colors

class CaveBlock(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 43, 274)

	def OnCollision(self, other):
		if (other.IsA("Player") and other.mVelocity[0] > 0):
			other.mVelocity[0] = 0s