import pygame
import os
import math

from GameState import *
from Player import *
from Level import *

from pygame.locals import *

import Colors

class GS_Game(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "Game", kernel, gsm)

		self.mLevel = None
		self.mPlayer = None

	def Initialize(self, levelName = ""):
		
		return GameState.Initialize(self)

	def LoadLevel(self, levelName):
		self.mLevel = Level(self.mKernel)
		self.mLevel.Load(levelName)

		self.mPlayer = Player(self.mKernel, self.mLevel)
		self.mPlayer.SetPosition([0, -100])
		return

	def Destroy(self):
		return GameState.Destroy(self)

	def Pause(self):
		return GameState.Pause(self)

	def Unpause(self):
		return GameState.Unpause(self)


	def HandleEvent(self, event):

		if (event.type == KEYDOWN):
			if (event.key == K_SPACE):
				self.mPlayer.Jump()
			elif (event.key == K_LEFT):
				self.mPlayer.Move("left")
			elif (event.key == K_RIGHT):
				self.mPlayer.Move("right")

		elif (event.type == KEYUP):
			if (event.key == K_LEFT):
				self.mPlayer.Stop("left")
			elif (event.key == K_RIGHT):
				self.mPlayer.Stop("right")

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mLevel.Update(delta)
		self.mPlayer.Update(delta)

		self.mLevel.Draw()
		self.mPlayer.Draw()

		self.mLevel.Blit()
		
		return GameState.Update(self, delta)
