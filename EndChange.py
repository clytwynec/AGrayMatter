import pygame

from LevelChangeTrigger import *

class EndChange (LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'EndTransition')