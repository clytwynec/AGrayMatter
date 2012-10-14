import pygame

from Entity import *

import Colors

class Moon3(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("moon.bmp")

	def OnCollision(self, other):
		other.Reset()

	def Update(self, delta):
		Entity.Update(self, delta)
		self.mPosition[1] += 8

		if (self.mPosition[1] > 600):
			self.mPosition[1] = -20