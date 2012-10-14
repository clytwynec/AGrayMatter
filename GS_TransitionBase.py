import pygame

from GameState import *

from pygame.locals import *

class GS_TransitionBase(GameState):
	def __init__(self, name, kernel, gsm, nextState):
		GameState.__init__(self, name, kernel, gsm)

		self.mFadeTime = 2000
		self.mTime = 8000
		self.mNextState = nextState

		self.mQuoteImage, self.mQuoteRect = self.mKernel.ImageManager().LoadImage(name + "_introtext.bmp")
		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage("motor_mask.bmp")
		self.mQuoteRect.center = (400, 300)

		self.mFadeOutStartTime = self.mTime - self.mFadeTime

		self.mSurface = pygame.Surface((800, 600))

	def Initialize(self):
		GameState.Initialize(self)

	def Unpause(self):

		GameState.Unpause(self)


	def HandleEvent(self, event):
				
		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mTime -= delta

		if (self.mTime <= 0):
			self.mGameStateManager.SwitchState(self.mNextState)

		self.mSurface.fill((64, 64, 64))
		self.mSurface.blit(self.mQuoteImage, self.mQuoteRect)

		alpha = None

		if (self.mTime >= self.mFadeOutStartTime):
			alpha = 255 * float(self.mFadeTime - (self.mTime - self.mFadeOutStartTime)) / float(self.mFadeTime)
		elif (self.mTime <= self.mFadeTime):
			alpha = 255 * float(self.mTime) / float(self.mFadeTime)

		if (alpha):
			self.mSurface.set_alpha(alpha)

		self.mSurface.blit(self.mMask, self.mMaskRect, None, BLEND_MULT)

		self.mKernel.DisplaySurface().blit(self.mSurface, self.mSurface.get_rect())

		GameState.Update(self, delta)