import pygame
from CraneBox import *
from CraneSwitch import *
from MotorDoor import *
from MaskedLevel import *
from MotorMan import *

import Colors

class MotorLevel(MaskedLevel):
	def __init__(self, kernel):
		MaskedLevel.__init__(self, kernel)
		
		self.mCraneSwitch = None
		self.mDoor = None
		self.mCraneBox = None
		self.mMotorMan = None
		self.mDoorTriggered = 0
		self.mDialogueTriggered = 4500

		self.mMotorWire, self.mMotorRect = self.mKernel.ImageManager().LoadImage('motor_wire.bmp')

		self.mMaskPosition = [400, 300]
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage('motor_mask.bmp', False)

		self.mSound = self.mKernel.SoundManager().LoadSound("HeartBeep.wav")

		self.mDialogueFont = pygame.font.SysFont("Times", 24, False)
		self.mDialogueText, self.mDialogueRect = self.mKernel.ImageManager().LoadImage('motor_text.bmp')
		self.mDialogueRect.center = (400, 60)

		self.mDialogueSurface = pygame.Surface((800,120)).convert()

	def Load(self, levelName):
		MaskedLevel.Load(self, levelName)

		self.mCraneSwitch = CraneSwitch(self.mKernel, self)
		self.mDoor = MotorDoor(self.mKernel, self)
		self.mCraneBox = CraneBox(self.mKernel, self)
		self.mMotorMan = MotorMan(self.mKernel, self)


		self.mCraneSwitch.SetPosition([348,27])
		self.mDoor.SetPosition([350,700])
		self.mCraneBox.SetPosition([675,325])
		self.mMotorMan.SetPosition([200, 248])

		self.mEntities.append(self.mCraneSwitch)
		self.mEntities.append(self.mDoor)
		self.mEntities.append(self.mCraneBox)
		self.mEntities.append(self.mMotorMan)


	def ShowDialogue(self):
		if(self.mDialogueTriggered>0):
			alpha = None
			self.mFadeTime = 1000
			self.mFadeOutStartTime = 1000

			self.mDialogueSurface.blit(self.mDialogueText, self.mDialogueRect)

			if (self.mDialogueTriggered>= 3500):
				alpha = 255 * float(4500-self.mDialogueTriggered) / float(self.mFadeTime)
			elif (self.mDialogueTriggered <= self.mFadeTime):
				alpha = 255 * float(self.mDialogueTriggered) / float(self.mFadeTime)

			if (alpha):
				self.mDialogueSurface.set_alpha(alpha)

			self.mLevelSurface.blit(self.mDialogueSurface, self.mDialogueSurface.get_rect())


	def Draw(self):
		MaskedLevel.Draw(self)
		self.mLevelSurface.blit(self.mMotorWire, self.mMotorRect)

		self.ShowDialogue()
		


	def Update(self, delta):
		MaskedLevel.Update(self, delta)

		if(self.mDialogueTriggered >0):
			self.mDialogueTriggered -= delta

		if(self.mDoorTriggered >= 2):
			self.mDoor.LiftDoor()