import pygame

from Level import *

import Colors

class VisualLevel(Level):
	def __init__(self, kernel):
		Level.__init__(self, kernel)
		
		self.mCraneSwitch = None
		self.mDoor = None
		self.mCraneBox = None

	def Load(self, levelName):
		level.load(self, levelName)