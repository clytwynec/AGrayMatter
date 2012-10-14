import pygame

from Entity import *

import Colors

class Moon2(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("moon.bmp")

	def OnCollision(self, other):
		other.Reset()

	def Update(self, delta):
		Entity.Update(self, delta)
		self.mPosition[1] -= 10

		if (self.mPosition[1] < -1 * self.mRect.height):
			self.mPosition[1] = 600