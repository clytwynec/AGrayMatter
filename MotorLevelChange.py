import pygame

from LevelChangeTrigger import *

class MotorLevelChange (LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'MotorTransition')