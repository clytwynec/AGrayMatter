import pygame

from LevelChangeTrigger import *

import Colors

class TestLevel2Trigger(LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'test_level2')