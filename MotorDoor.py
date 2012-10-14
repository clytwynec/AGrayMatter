import pygame

from LevelChangeTrigger import *

import Colors

class MotorDoor(LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'test_level2')

		self.mRising = False

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage('tallDoor.bmp')

	def LiftDoor(self):
		self.mRising = True

	def Trigger(self, other):
		LevelChangeTrigger.Trigger(self, other)

	def Update(self, delta):
		LevelChangeTrigger.Update(self, delta)
		if(self.mRising == True and self.mPosition[1]>375):
			self.mPosition[1] -= 1
