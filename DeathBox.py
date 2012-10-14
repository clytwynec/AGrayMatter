import pygame
from pygame.locals import *

from Entity import *

import Colors

class DeathBox(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 25, 32)

	def OnCollision(self, other):
		if (other.IsA("Player")):
			other.Reset()

	def Draw(self):
		Entity.Draw(self)

		# pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)