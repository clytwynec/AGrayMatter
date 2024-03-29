###################################################################################
# Game.py
#
# The kickoff script/main loop.  Sets up the different game systems, and then
# enters the main loop.  Runs until we receive a system event to quit the game
#
# Command Line Arguments
###################################################################################

# System level imports
from optparse import OptionParser
import sys
import os
import math
import pygame
import random 

from pygame.locals import *

# App level imports
from GameKernel import *
from GameStateManager import *
from GS_Game import *
from GS_Editor import *
from GS_AudioTransition import *
from GS_AudioLevel import *
from GS_DelayLevel import *
from GS_MotorLevel import *
from GS_MainMenu import *
from GS_MotorTransition import *
from GS_DelayTransition import *
from GS_EndTransition import *
from GS_End import *
from GS_GameOverTransition import *


#random.seed(0)

#########################
# Start Main
#########################

#### Parse command line arguments
optionParser = OptionParser()
# optionParser.add_option("-e", "--editlevel", help="Edit the level with a specified filename.  If no such level exists, create a new one.")
# optionParser.add_option("-l", "--levellength", help="When editing a level, this is the length of the level")
(options, args) = optionParser.parse_args()

def main():
	#### Kick off the graphics/window system
	kernel = GameKernel()
	screenSurface = kernel.InitializeDisplay((800, 600))
	ticker = kernel.Ticker()

	#### Initialize game states
	gsm = GameStateManager()
	gsm.RegisterState(GS_MainMenu(kernel, gsm))
	gsm.RegisterState(GS_Game(kernel, gsm))
	gsm.RegisterState(GS_Editor(kernel, gsm))
	gsm.RegisterState(GS_DelayLevel(kernel, gsm))
	gsm.RegisterState(GS_AudioTransition(kernel, gsm))
	gsm.RegisterState(GS_MotorTransition(kernel, gsm))
	gsm.RegisterState(GS_DelayTransition(kernel, gsm))
	gsm.RegisterState(GS_EndTransition(kernel, gsm))
	gsm.RegisterState(GS_AudioLevel(kernel, gsm))
	gsm.RegisterState(GS_MotorLevel(kernel, gsm))
	gsm.RegisterState(GS_End(kernel, gsm))
	gsm.RegisterState(GS_GameOverTransition(kernel, gsm))

	kernel.SetGameStateManager(gsm)

	gsm.SwitchState("MainMenu")

	font = pygame.font.SysFont("Helvetica", 12)

	## Main Loop
	while (1):

		delta = ticker.get_time()
		
		gsm.Update(delta)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			else:
				gsm.GetActiveState().HandleEvent(event)

		FPSSurf = font.render("FPS: " + str(int(ticker.get_fps())), True, (255, 255, 255))
		FPSRect = FPSSurf.get_rect()
		FPSRect.topright = screenSurface.get_rect().topright
		screenSurface.blit(FPSSurf, FPSRect)

		kernel.FlipDisplay()

		ticker.tick(60)

main()

# import cProfile as profile
# profile.run('main()', 'profile.out')