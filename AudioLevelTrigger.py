import pygame

from Entity import *

import Colors

class AudioLevelTrigger(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		
		self.mInteractable = False
		self.mRect = pygame.Rect(0, 0, 20, 2)

		self.mTriggered = False

		self.mNextNode = None

	def Trigger(self, other):
		self.mLevel.mMaskPosition = list(self.mRect.center)
		# self.mTriggered = True

	def OnCollision(self, other):
		if (self.mTriggered == False):
			# self.mTriggered = True

			if (self.mNextNode):
				self.mNextNode.Trigger(None)

	def Draw(self):
		Entity.Draw(self)

		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.YELLOW, self.mRect, 2)