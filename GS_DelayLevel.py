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

class GS_DelayLevel(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "DelayLevel", kernel, gsm)

		self.mLevel = None
		self.mPlayer = None

		self.mTicks = 0
		self.mEventsQueue = []

	def Initialize(self, levelName = ""):
		
		return GameState.Initialize(self)

	def LoadLevel(self, levelName):
		self.mLevel = Level(self.mKernel)
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

	def HandleOffsetEvent(self, event):

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

	def HandleEvent(self, event):
		if (event.type == KEYDOWN or event.type == KEYUP):
			self.mEventsQueue.append({
				"tick": self.mTicks + 500,
				"event": event
			});

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mTicks += delta

		for event in self.mEventsQueue:
			if (event["tick"] <= self.mTicks):
				self.HandleOffsetEvent(event["event"])
				self.mEventsQueue.remove(event)
			else:
				break

		self.mPlayer.Update(delta)
		self.mLevel.Update(delta)

		# self.mLevel.mPlayerRect.center = self.mPlayer.mRect.center

		self.mLevel.Draw()
		self.mPlayer.Draw()

		self.mLevel.Blit()
		
		# self.mLevel.mMaskPosition = [-100, -100]

		return GameState.Update(self, delta)
