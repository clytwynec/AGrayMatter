import pygame

from Entity import *

import Colors

class TriggerTest(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True
		self.mRect = pygame.Rect(0, 0, 100, 100)

	def Trigger(self, other):
		print "Triggered!"

	def Draw(self):
		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)