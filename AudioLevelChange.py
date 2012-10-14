import pygame

from LevelChangeTrigger import *

class AudioLevelChange (LevelChangeTrigger):
	def __init__(self, kernel, level):
		LevelChangeTrigger.__init__(self, kernel, level, 'AudioTransition')