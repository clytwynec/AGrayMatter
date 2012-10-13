import pygame
import sys
import math

from Entity import *
from Colors import *

class Player(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)

		self.mVelocity = [0, 0]

		self.mCollisionRect = pygame.Rect(0, 0, 50, 125)
		return

	def Update(self, delta):
		self.mVelocity[1] += 3.0 * delta
		self.mPosition[1] += self.mVelocity[1] * delta

		return Entity.Update(self, delta)

	def Draw(self):
		Entity.Draw(self)

		pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.BLUE, self.mCollisionRect, 2)
		return