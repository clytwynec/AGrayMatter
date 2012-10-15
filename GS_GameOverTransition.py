from GS_TransitionBase import *

import Colors

from pygame.locals import *

class GS_GameOverTransition(GS_TransitionBase):
	def __init__(self, kernel, gsm):
		GS_TransitionBase.__init__(self, "GameOverTransition", kernel, gsm, "MainMenu")

		self.mSurface.set_alpha(0)

		self.mMask, self.mMaskRect = self.mKernel.ImageManager().LoadImage("end_mask.bmp")
		self.mBackground, self.mBackgroundRect = self.mKernel.ImageManager().LoadImage("gobackground.bmp")

		self.mFadeTime = 4000
		self.mTime = 10000

		self.mSound = self.mKernel.SoundManager().LoadSound("HeartBeep.wav")

	def Initialize(self):
		self.mSound.play()

		return GS_TransitionBase.Initialize(self)

	def Pause(self):

		return GS_TransitionBase.Pause(self)

	def Update(self, delta):
		self.mTime -= delta

		if (self.mTime <= 0 and self.mTime >= -60):
			self.mSound.fadeout(5000)

		if (self.mTime <= -5000):
			self.mGameStateManager.SwitchState(self.mNextState)

		alpha = None

		if (self.mTime >= self.mFadeOutStartTime):
			alpha = 255 * float(self.mFadeTime - (self.mTime - self.mFadeOutStartTime)) / float(self.mFadeTime)
		elif (self.mTime <= self.mFadeTime):
			alpha = 255 * float(self.mTime) / float(self.mFadeTime)

		if (alpha):
			self.mSurface.set_alpha(alpha)

		if (self.mTime <= self.mFadeOutStartTime):
			self.mSurface.fill(Colors.BLACK)
			self.mSurface.blit(self.mBackground, self.mBackgroundRect)
		else:
			self.mKernel.DisplaySurface().blit(self.mBackground, self.mBackgroundRect)

		self.mSurface.blit(self.mQuoteImage, self.mQuoteRect)
		self.mSurface.blit(self.mMask, self.mMaskRect, None, BLEND_MULT)

		self.mKernel.DisplaySurface().blit(self.mSurface, self.mSurface.get_rect())

		GameState.Update(self, delta)