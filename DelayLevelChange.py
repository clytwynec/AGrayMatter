import pygame

from LevelChangeTrigger import *

class DelayLevelChange (LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'DelayTransition')