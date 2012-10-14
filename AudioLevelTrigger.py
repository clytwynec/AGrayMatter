import pygame
from pygame.locals import *
import random

from Entity import *

import Colors

class AudioLevelTrigger(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False

		self.mRect = pygame.Rect(0, 0, 20, 20)

		self.mOffset = 1000
		self.mTick = 0

		self.mCountdown = 0

		self.mMaskImage, self.mMaskRect = self.mKernel.ImageManager().LoadImage("mask.bmp")
		self.mSound = self.mKernel.SoundManager().LoadSound("drop" + str(random.randrange(1, 4)) + ".wav")

	def SetPosition(self, position):
		Entity.SetPosition(self, position)
		self.mMaskRect.center = self.mRect.center

	def Update(self, delta):
		Entity.Update(self, delta)

		self.mTick += delta

		if (self.mTick >= self.mOffset):
			self.mCountdown = 1000
			self.mSound.play()
			self.mTick = 0

		if (self.mCountdown >= 0):
			self.mCountdown -= delta


	def Draw(self):
		Entity.Draw(self)

		if (self.mCountdown > 0):
			self.mLevel.mMaskSurface.blit(self.mMaskImage, self.mMaskRect, None, BLEND_ADD)