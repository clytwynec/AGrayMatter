import pygame

from Entity import *

import Colors

class LevelChangeTrigger(Entity):
	def __init__(self, kernel, level, newLevelName):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True
		self.mRect = pygame.Rect(0, 0, 100, 100)

		self.mNewLevel = newLevelName

	def Trigger(self, other):
		self.mLevel.Unload()
		self.mLevel.Load(self.mNewLevel)

	def Draw(self):
		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)