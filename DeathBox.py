import pygame
from pygame.locals import *

from Entity import *

import Colors

class DeathBox(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 20, 10)

	def SetPosition(self, position):
		Entity.SetPosition(self, position)
		self.mMaskRect.center = self.mRect.center

	def Update(self, delta):
		Entity.Update(self, delta)

		self.mTick += delta

		if (self.mTick >= self.mOffset):
			self.mCountdown = 1000
			self.mTick = 0

		if (self.mCountdown >= 0):
			self.mCountdown -= delta


	def Draw(self):
		Entity.Draw(self)

		if (self.mCountdown > 0):
			self.mLevel.mMaskSurface.blit(self.mMaskImage, self.mMaskRect, None, BLEND_ADD)

		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)