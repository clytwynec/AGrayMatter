import pygame
import os
import math

from GameState import *
from Player import *
from Level import *
from MaskedLevel import *
from AudioLevel import *
from MotorLevel import *

from pygame.locals import *

import Colors

class GS_MotorLevel(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "MotorLevel", kernel, gsm)

		self.mLevel = None
		self.mPlayer = None

	def Initialize(self, levelName = ""):
		
		self.LoadLevel("motor")

		return GameState.Initialize(self)

	def LoadLevel(self, levelName):
		self.mLevel = MotorLevel(self.mKernel)
		self.mLevel.Load(levelName)

		self.mPlayer = Player(self.mKernel, self.mLevel)
		self.mPlayer.Reset()
		return

	def Destroy(self):
		return GameState.Destroy(self)

	def Pause(self):
		return GameState.Pause(self)

	def Unpause(self):
		return GameState.Unpause(self)

	def HandleEvent(self, event):

		if (event.type == KEYDOWN):
			if (event.key == K_UP):
				self.mPlayer.Jump()
			elif (event.key == K_LEFT):
				self.mPlayer.Move("left")
			elif (event.key == K_RIGHT):
				self.mPlayer.Move("right")
			elif (event.key == K_SPACE):
				self.mPlayer.Interact()

		elif (event.type == KEYUP):
			if (event.key == K_LEFT):
				self.mPlayer.Stop("left")
			elif (event.key == K_RIGHT):
				self.mPlayer.Stop("right")

		return GameState.HandleEvent(self, event)

	def Update(self, delta):

		self.mPlayer.Update(delta)
		self.mLevel.Update(delta)

		self.mLevel.mPlayerRect.center = self.mPlayer.mRect.center

		self.mLevel.Draw()
		self.mPlayer.Draw()

		self.mLevel.Blit()
		
		# self.mLevel.mMaskPosition = [-100, -100]

		return GameState.Update(self, delta)
