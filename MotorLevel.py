import pygame
from CraneBox import *
from CraneSwitch import *
from MotorDoor import *
from Level import *

import Colors

class MotorLevel(Level):
	def __init__(self, kernel):
		Level.__init__(self, kernel)
		
		self.mCraneSwitch = None
		self.mDoor = None
		self.mCraneBox = None

	def Load(self, levelName):
		Level.Load(self, levelName)

		self.mCraneSwitch = CraneSwitch(self.mKernel, self)
		self.mDoor = MotorDoor(self.mKernel, self)
		self.mCraneBox = CraneBox(self.mKernel, self)

		self.mCraneSwitch.SetPosition([100,100])
		self.mDoor.SetPosition([200,200])
		self.mCraneBox.SetPosition([300,300])