import pygame
from Entity import *


class MotorMan(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)

		self.mInteractable = True
		self.mRect = pygame.Rect(0, 0, 64, 75)

	def Trigger(self, other):
		self.mLevel.mDialogueTriggered = 4500