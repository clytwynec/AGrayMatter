import pygame
import random

from MaskedLevel import *
import Colors

from pygame.locals import *

class AudioLevel(MaskedLevel):
	def __init__(self, kernel):
		MaskedLevel.__init__(self, kernel)
		
		self.mAudioTriggers = []
		self.mCurrentPlatform = None

	def Load(self, levelName):
		Level.Load(self, levelName)

		self.SetTriggers()

	def SetTriggers(self):
		for entity in self.mEntities:
			if (entity.IsA("AudioLevelTrigger")):
				entity.mOffset = random.randrange(6000, 20000, 500)
				entity.mTick = random.randrange(0, entity.mOffset, 250)

	def Draw(self):
		self.mMaskSurface.fill(Colors.BLACK)
		Level.Draw(self)

		self.mMaskSurface.blit(self.mPlayerMask, self.mPlayerRect, None, BLEND_ADD)

		self.mLevelSurface.blit(self.mMaskSurface, self.mMaskSurface.get_rect(), None, BLEND_MULT)
