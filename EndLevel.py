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
