import pygame

from Entity import *

import Colors

class CraneSwitch(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = True
		self.mOffImage, self.mRect = self.mKernel.ImageManager().LoadImage('switch_off.bmp')
		self.mOnImage, self.mOnRect = self.mKernel.ImageManager().LoadImage('switch_on.bmp')
		self.mImage = self.mOffImage
	def Trigger(self, other):
		self.mImage = self.mOnImage