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
		self.mDoorTriggered = 0

		self.mMotorWire, self.mMotorRect = self.mKernel.ImageManager().LoadImage('motor_wire.bmp')


	def Load(self, levelName):
		Level.Load(self, levelName)

		self.mCraneSwitch = CraneSwitch(self.mKernel, self)
		self.mDoor = MotorDoor(self.mKernel, self)
		self.mCraneBox = CraneBox(self.mKernel, self)


		self.mCraneSwitch.SetPosition([348,27])
		self.mDoor.SetPosition([350,700])
		self.mCraneBox.SetPosition([675,325])

		self.mEntities.append(self.mCraneSwitch)
		self.mEntities.append(self.mDoor)
		self.mEntities.append(self.mCraneBox)


	def Draw(self):
		Level.Draw(self)
		self.mLevelSurface.blit(self.mMotorWire, self.mMotorRect)

	def Update(self, delta):
		Level.Update(self, delta)

		if(self.mDoorTriggered >= 2):
			self.mDoor.LiftDoor()