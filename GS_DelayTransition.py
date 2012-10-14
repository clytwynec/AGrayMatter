from GS_TransitionBase import *

from pygame.locals import *

class GS_DelayTransition(GS_TransitionBase):
	def __init__(self, kernel, gsm):
		GS_TransitionBase.__init__(self, "DelayTransition", kernel, gsm, "DelayLevel")