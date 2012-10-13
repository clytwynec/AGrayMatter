import pygame

from Level import *
import Colors

from pygame.locals import *

class MaskedLevel(Level):
	def __init__(self, kernel):
		Level.__init__(self, kernel)
		
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage("mask.bmp")
		self.mMaskSurface = pygame.Surface((800, 600)).convert(self.mLevelSurface)

		self.mMaskPosition = [100, 100]

	def Update(self, delta):
		Level.Update(self, delta)

		self.mMaskRect.center = self.mMaskPosition

		return

	def Draw(self):
		Level.Draw(self)

		self.mMaskSurface.fill(Colors.BLACK)
		self.mMaskSurface.blit(self.mMask, self.mMaskRect)
		self.mLevelSurface.blit(self.mMaskSurface, self.mMaskSurface.get_rect(), None, BLEND_MULT)

		return