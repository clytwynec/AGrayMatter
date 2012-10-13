import pygame

from Entity import *

import Colors

class CraneSwitch(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True
		self.mRect = pygame.Rect(0, 0, 100, 100)

	def Trigger(self, other):
		print "Triggered!"
