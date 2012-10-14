import pygame

from LevelChangeTrigger import *

import Colors

class MotorDoor(LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'test_level2')

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage('tallDoor.bmp')


	def Trigger(self, other):
		LevelChangeTrigger.Trigger(self, other)