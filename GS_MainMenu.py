from GS_MenuBase import *
from Player import *
from MaskedLevel import *

class GS_MainMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "MainMenu", kernel, gsm)

		self.mHeading, self.mHeadingRect = kernel.ImageManager().LoadImage("GrayMatter.bmp", False)
		self.mCompanyImage, self.mCompanyRect = kernel.ImageManager().LoadImage("company.bmp", False)
		self.mCompanyImage.set_alpha(0)
		self.mHeadingRect.topleft = [ 400 - (self.mHeadingRect.width / 2.0), 20 ]
		self.mCompanyRect.topleft = [ 400 - (self.mCompanyRect.width / 2.0), 155 ]
		self.mLevel = None
		self.mPlayer = None
		self.mTime = -7000

	def Initialize(self):
		self.mLevel = MaskedLevel(self.mKernel)
		self.mLevel.Load("main_menu")
		self.mLevel.mMaskPosition = [700, 500]
		self.mLevel.mMaskRect.center = self.mLevel.mMaskPosition

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

		self.mTime += delta

		self.mLevel.mPlayerRect.center = self.mPlayer.mRect.center

		self.mLevel.Draw()
		self.mPlayer.Draw()

		# self.mSurface.fill((64, 64, 64))
		# self.mSurface.blit(self.mCompanyImage, self.mCompanyRect)

		alpha = None

		if (self.mTime > 0 and self.mTime <= 3000):
			alpha = 255 * self.mTime / 3000.0
		 
		if (alpha):
			self.mCompanyImage.set_alpha(alpha)

		# self.mKernel.DisplaySurface().blit(self.mSurface, self.mSurface.get_rect())

		self.mLevel.DisplaySurface().blit(self.mCompanyImage, self.mCompanyRect)

		self.mLevel.Blit()
		
		return GS_MenuBase.Update(self, delta)
