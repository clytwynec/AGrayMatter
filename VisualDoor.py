import pygame

from LevelChangeTrigger import *

import Colors

class VisualDoor(LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'test_level2')