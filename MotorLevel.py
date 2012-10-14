import pygame
from CraneBox import *
from CraneSwitch import *
from MotorDoor import *
from MaskedLevel import *

import Colors

class MotorLevel(MaskedLevel):
	def __init__(self, kernel):
		MaskedLevel.__init__(self, kernel)
		
		self.mCraneSwitch = None
		self.mDoor = None
		self.mCraneBox = None
		self.mDoorTriggered = 0

		self.mMotorWire, self.mMotorRect = self.mKernel.ImageManager().LoadImage('motor_wire.bmp')

		self.mMaskPosition = [400, 300]
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage('motor_mask.bmp', False)

		self.mDialogueMask, self.mDialogueMaskRect = self.mKernel.ImageManager().LoadImage('text_box_template.bmp', False)
		self.mDialogueText, self.mDialogueTextRect = self.mKernel.ImageManager().LoadImage('text_box_Layer.bmp')


		self.mDialogueFont = pygame.font.SysFont("Courier New", 24, True)
		self.mDialogueSurface = None

	def Load(self, levelName):
		MaskedLevel.Load(self, levelName)

		self.mCraneSwitch = CraneSwitch(self.mKernel, self)
		self.mDoor = MotorDoor(self.mKernel, self)
		self.mCraneBox = CraneBox(self.mKernel, self)


		self.mCraneSwitch.SetPosition([348,27])
		self.mDoor.SetPosition([350,700])
		self.mCraneBox.SetPosition([675,325])

		self.mEntities.append(self.mCraneSwitch)
		self.mEntities.append(self.mDoor)
		self.mEntities.append(self.mCraneBox)


	def ShowDialogue(self):
		self.mLevelSurface.blit(self.mDialogueText, self.mDialogueTextRect)
		self.mLevelSurface.blit(self.mDialogueMask, self.mDialogueMaskRect, None, BLEND_MULT)

	def Draw(self):
		MaskedLevel.Draw(self)
		self.mLevelSurface.blit(self.mMotorWire, self.mMotorRect)

		self.ShowDialogue()
		


	def Update(self, delta):
		MaskedLevel.Update(self, delta)

		if(self.mDoorTriggered >= 2):
			self.mDoor.LiftDoor()