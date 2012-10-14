from GS_TransitionBase import *

from pygame.locals import *

class GS_MotorTransition(GS_TransitionBase):
	def __init__(self, kernel, gsm):
		GS_TransitionBase.__init__(self, "MotorTransition", kernel, gsm, "MotorLevel")