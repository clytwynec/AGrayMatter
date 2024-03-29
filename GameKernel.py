###################################################################################
# GameKernel
#
# Handles system level interfaces for the graphics, system event, 
# and input subsystems.  Provides the basic interface into pygame
#
###################################################################################
import pygame
import sys

import Colors

from pygame.locals import *
from ImageManager import *
from SoundManager import *

class GameKernel:
	def __init__(self):
		pygame.init()

		print "Pygame Version: " + pygame.version.ver

		self.mDisplaySurface = None
		self.mTicker = pygame.time.Clock()
		self.mImageManager = ImageManager(self)
		self.mSoundManager = SoundManager(self)

		self.mGameStateManager = None

	#####################################################
	# InitializeDisplay
	#
	# Creates the display window.  If a display is already
	# initialized, this reinitializes the display.
	# If you do this, make sure to propogate the new surface
	# down through the various subsystems that need the
	# display surface
	#
	# Parameters:
	#	dimensions - a 2-tuple of the desired dimenions
	#	fullscreen - fullscreen toggle
	#
	# Returns:
	#	display - The display surface.  Required to allow
	#		other contexts to blit to the screen
	###################################################### 
	def InitializeDisplay(self, dimensions, fullscreen=False):
		flags = pygame.DOUBLEBUF

		if (fullscreen):
			flags = flags | pygame.FULLSCREEN 

		self.mDisplaySurface = pygame.display.set_mode(dimensions, flags)

		assert self.mDisplaySurface, "Display failed to intialize."

		return self.mDisplaySurface


	#####################################################
	# GetDisplaySurface
	#
	# Returns the current display surface
	#####################################################
	def DisplaySurface(self):
		return self.mDisplaySurface

	#####################################################
	# GetTicker
	#
	# Returns the system ticker.
	#####################################################
	def Ticker(self):
		return self.mTicker

	#####################################################
	# ImageManager
	#
	# Returns the image manager.
	#####################################################
	def ImageManager(self):
		return self.mImageManager

	def SoundManager(self):
		return self.mSoundManager

	def SetGameStateManager(self, gsm):
		self.mGameStateManager = gsm

	def GameStateManager(self):
		if (self.mGameStateManager):
			return self.mGameStateManager

	#####################################################
	# FlipDisplay
	#
	# Flips the display surface
	#####################################################
	def FlipDisplay(self):
		pygame.display.flip()
		
		self.mDisplaySurface.fill(Colors.BLACK)

	#####################################################
	# ProcessSystemEvents
	# 
	# Processes system events and dispatches them to the
	# system or input subsystems as appropriate
	#####################################################
	def ProcessSystemEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()