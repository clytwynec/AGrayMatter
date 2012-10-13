import pygame

from Entity import *

import Colors

class LevelChangeTrigger(Entity):
	def __init__(self, kernel, level, newLevelName):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("door.bmp")

		self.mNewLevel = newLevelName

	def Trigger(self, other):
		self.mLevel.Unload()
		self.mLevel.Load(self.mNewLevel)

		self.mKernel.GameStateManager().GetActiveState().mPlayer.Reset()

	def Draw(self):
		Entity.Draw(self)

		# pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)

		return