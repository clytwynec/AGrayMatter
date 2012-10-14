from GS_TransitionBase import *

from pygame.locals import *

class GS_EndTransition(GS_TransitionBase):
	def __init__(self, kernel, gsm):
		GS_TransitionBase.__init__(self, "EndTransition", kernel, gsm, "End")