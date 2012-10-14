import pygame
from pygame.locals import *

from Entity import *

import Colors

class SafePoint(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 32, 32)
		self.mSaved = False

		self.mOffImage, self.mRect = self.mKernel.ImageManager().LoadImage('SafePointOff.bmp')
		self.mOnImage, self.mOnRect = self.mKernel.ImageManager().LoadImage('SafePointOn.bmp')
		self.mImage = self.mOffImage


	def OnCollision(self, other):
		if (other.IsA("Player")):
			if(not self.mSaved):
				self.mImage = self.mOnImage
				self.mLevel.mStartPosition = self.mPosition
				self.mSaved = True