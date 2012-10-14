from GS_MenuBase import *
from Player import *
from AudioLevel import *

class GS_MainMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "MainMenu", kernel, gsm)

		self.mHeadingImage, self.mHeadingRect = kernel.ImageManager().LoadImage("GrayMatter.bmp", False)
		self.mHeadingRect.topleft = [ 400 - (self.mHeadingRect.width / 2.0), 20 ]
		self.mLevel = None
		self.mPlayer = None

	def Initialize(self):
		self.mLevel = AudioLevel(self.mKernel)
		self.mLevel.Load("main_menu")
		self.mLevel.mMaskPosition = [700, 500]

		self.mPlayer = Player(self.mKernel, self.mLevel)
		self.mPlayer.Reset()

		GS_MenuBase.Initialize(self)

	def Unpause(self):

		GS_MenuBase.Unpause(self)


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
				
		return GS_MenuBase.HandleEvent(self, event)

	def Update(self, delta):
		self.mPlayer.Update(delta)
		self.mLevel.Update(delta)

		self.mLevel.mPlayerRect.center = self.mPlayer.mRect.center

		self.mLevel.Draw()
		self.mPlayer.Draw()

		self.mLevel.DisplaySurface().blit(self.mHeadingImage, self.mHeadingRect)

		self.mLevel.Blit()

		GS_MenuBase.Update(self, delta)