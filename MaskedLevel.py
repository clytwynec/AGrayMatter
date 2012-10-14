import pygame

from Level import *
import Colors

from pygame.locals import *

class MaskedLevel(Level):
	def __init__(self, kernel):
		Level.__init__(self, kernel)
		
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage("mask.bmp", False)
		self.mMaskSurface = pygame.Surface((800, 600)).convert(self.mLevelSurface)

		self.mPlayerMask, self.mPlayerRect = self.mKernel.ImageManager().LoadImage("player_mask.bmp", False)

		self.mMaskPosition = [100, 100]

	def Update(self, delta):
		Level.Update(self, delta)

		# self.mMaskRect.center = self.mMaskPosition

		return

	def Draw(self):
		Level.Draw(self)

		self.mMaskSurface.fill(Colors.BLACK)
		self.mMaskSurface.blit(self.mMask, self.mMaskRect)
		self.mMaskSurface.blit(self.mPlayerMask, self.mPlayerRect, None, BLEND_ADD)
		self.mLevelSurface.blit(self.mMaskSurface, self.mMaskSurface.get_rect(), None, BLEND_MULT)

		return