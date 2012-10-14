import pygame
import os
import math

from GameState import *
from Player import *
from Level import *
from EndLevel import *

from pygame.locals import *

import Colors

class GS_End(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "End", kernel, gsm)

		self.mLevel = None
		self.mPlayer = None

		self.mTick = 0
		self.mSavedEvents = []

		self.mPlayerEvents = []
		self.mOtherEvents = []

		self.mGlowTime = 12000
		self.mGlowSpeed = 2000

		self.mStopTime = 24000

		self.mScreechSound = self.mKernel.SoundManager().LoadSound("CarScreech.wav")
		self.mScreechSound.set_volume(0.5)
		self.mPlaying = False

	def Initialize(self, levelName = ""):
		GameState.Initialize(self)

		self.LoadLevel("end")

		return

	def LoadLevel(self, levelName):
		self.mLevel = EndLevel(self.mKernel)
		self.mLevel.Load(levelName)

		self.mPlayer = Player(self.mKernel, self.mLevel)
		self.mPlayer.mMoveThrottle = 2
		self.mPlayer.Reset()

		self.mOtherPlayer = Player(self.mKernel, self.mLevel)
		self.mOtherPlayer.mMoveThrottle = 1
		self.mOtherPlayer.mLeftImage, rect = self.mKernel.ImageManager().LoadImage("player_grey_left.bmp")
		self.mOtherPlayer.mRightImage, rect = self.mKernel.ImageManager().LoadImage("player_grey_right.bmp")
		self.mOtherPlayer.Reset()
		self.mOtherPlayer.SetPosition([ 800, self.mOtherPlayer.mPosition[1] ])

		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage("headlight.bmp")
		self.mMaskSurf = self.mMask.copy()

		self.LoadPlayerEvents()
		return

	def Destroy(self):
		return GameState.Destroy(self)

	def Pause(self):
		return GameState.Pause(self)

	def Unpause(self):
		return GameState.Unpause(self)

	def LoadPlayerEvents(self):
		self.mPlayerEvents = [
			{ "time": 1989, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 2061, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 2994, "event": pygame.event.Event(2, { "key": 275 }) },
			{ "time": 3061, "event": pygame.event.Event(3, { "key": 275 }) },
			{ "time": 4707, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 4773, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 5522, "event": pygame.event.Event(2, { "key": 275 }) },
			{ "time": 5640, "event": pygame.event.Event(3, { "key": 275 }) },
			{ "time": 6945, "event": pygame.event.Event(2, { "key": 275 }) },
			{ "time": 8351, "event": pygame.event.Event(3, { "key": 275 }) },
			{ "time": 10078, "event": pygame.event.Event(2, { "key": 275 }) },
			{ "time": 10295, "event": pygame.event.Event(3, { "key": 275 }) }
		]

		self.mOtherEvents = [
			{ "time": 577, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 796, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 1351, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 1649, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 2123, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 2342, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 2825, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 2975, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 3810, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 4312, "event": pygame.event.Event(3, { "key": 276 }) },
			{ "time": 4712, "event": pygame.event.Event(2, { "key": 276 }) },
			{ "time": 9202, "event": pygame.event.Event(3, { "key": 276 }) }
		]

	def HandlePlayerEvent(self, event):

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

	def HandleOtherEvent(self, event):

		if (event.type == KEYDOWN):
			if (event.key == K_UP):
				self.mOtherPlayer.Jump()
			elif (event.key == K_LEFT):
				self.mOtherPlayer.Move("left")
			elif (event.key == K_RIGHT):
				self.mOtherPlayer.Move("right")
			elif (event.key == K_SPACE):
				self.mOtherPlayer.Interact()

		elif (event.type == KEYUP):
			if (event.key == K_LEFT):
				self.mOtherPlayer.Stop("left")
			elif (event.key == K_RIGHT):
				self.mOtherPlayer.Stop("right")

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mTick += delta

		if (self.mTick >= self.mStopTime):
			self.mGameStateManager.SwitchState("MainMenu")

		for event in self.mPlayerEvents:
			if (event["time"] <= self.mTick):
				self.HandlePlayerEvent(event["event"])
				self.mPlayerEvents.remove(event)

		for event in self.mOtherEvents:
			if (event["time"] <= self.mTick):
				self.HandleOtherEvent(event["event"])
				self.mOtherEvents.remove(event)

		self.mPlayer.Update(delta)
		self.mOtherPlayer.Update(delta)
		self.mLevel.Update(delta)

		self.mLevel.mPlayerRect.center = self.mPlayer.mRect.center

		if (self.mTick < self.mLevel.mFadeStartTime):
			self.mLevel.Draw()
			self.mPlayer.Draw()
			self.mOtherPlayer.Draw()

		if (self.mTick >= self.mGlowTime):
			if (not self.mPlaying):
				self.mScreechSound.play()
				self.mPlaying = True

			if (self.mTick <= self.mGlowTime + self.mGlowSpeed):
				alpha = 255 * float(self.mTick - self.mGlowTime) / float(self.mGlowSpeed)
				self.mMaskSurf.set_alpha(alpha)

			self.mMaskSurf.blit(self.mMask, (0, 0, self.mMaskRect.width, self.mMaskRect.height))

			self.mMaskRect.center = self.mPlayer.mRect.center
			self.mLevel.DisplaySurface().blit(self.mMaskSurf, self.mMaskRect)

			self.mMaskRect.center = self.mOtherPlayer.mRect.center
			self.mLevel.DisplaySurface().blit(self.mMaskSurf, self.mMaskRect)

		if (self.mTick >= self.mLevel.mFadeStartTime):
			self.mLevel.DrawFade()

		self.mLevel.Blit()

		return GameState.Update(self, delta)
