import pygame
import os
import math

from GameState import *
from Player import *
from Level import *

from pygame.locals import *

import Colors

class GS_Editor(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "Editor", kernel, gsm)

		self.mLevel = None
		self.mRects = []

		self.mLastPoint = None

	def Initialize(self, levelName = ""):
		
		return GameState.Initialize(self)

	def LoadLevel(self, levelName):
		self.mLevel = Level(self.mKernel)
		self.mLevel.Load(levelName)

		self.mRects = self.mLevel.mCollisionRects

		return

	def Destroy(self):
		return GameState.Destroy(self)

	def Pause(self):
		return GameState.Pause(self)

	def Unpause(self):
		return GameState.Unpause(self)


	def HandleEvent(self, event):

		if (event.type == MOUSEBUTTONDOWN):
			if (self.mLastPoint):
				width = event.pos[0] - self.mLastPoint[0]
				height = event.pos[1] - self.mLastPoint[1]

				self.mRects.append(pygame.Rect(self.mLastPoint[0], self.mLastPoint[1], width, height))

				self.mLastPoint = None
			else:
				self.mLastPoint = event.pos
		elif (event.type == KEYDOWN):
			if (event.key == K_BACKSPACE):
				self.mRects.pop()
			elif (event.key == K_RETURN):
				self.mLevel.Save(self.mRects)

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mLevel.Draw()

		for rect in self.mRects:
			pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.RED, rect, 2)

		self.mLevel.Blit()
		
		return GameState.Update(self, delta)
