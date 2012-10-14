import pygame
import random

from MaskedLevel import *
import Colors

from pygame.locals import *

class EndLevel(MaskedLevel):
	def __init__(self, kernel):
		MaskedLevel.__init__(self, kernel)

		self.mMaskPosition = [400, 300]
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage('end_mask.bmp', False)

		self.mFadeStartTime = 17000
		self.mFadeEndTime = 20000

		self.mTime = 0

	def Update(self, delta):
		self.mTime += delta

		return MaskedLevel.Update(self, delta)

	def DrawFade(self):
		if (self.mTime <= self.mFadeEndTime):
			self.mMaskSurface.blit(self.mMask, self.mMaskRect)
			self.mMaskSurface.blit(self.mPlayerMask, self.mPlayerRect, None, BLEND_ADD)
		else:
			self.mLevelSurface.fill(Colors.BLACK)
				
	def Draw(self):
		Level.Draw(self)
		self.mMaskSurface.fill(Colors.BLACK)
		self.mMaskSurface.blit(self.mMask, self.mMaskRect)
		self.mMaskSurface.blit(self.mPlayerMask, self.mPlayerRect, None, BLEND_ADD)

	def Blit(self):
		if (self.mTime <= self.mFadeEndTime):
			if (self.mTime <= self.mFadeStartTime):
				self.mLevelSurface.blit(self.mMaskSurface, self.mMaskSurface.get_rect(), None, BLEND_MULT)
			else:
				self.mLevelSurface.blit(self.mMaskSurface, self.mMaskSurface.get_rect(), None, BLEND_ADD)
		else:
			self.mLevelSurface.fill(Colors.BLACK)

		MaskedLevel.Blit(self)
