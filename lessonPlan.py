

class lessonPlan:

	def __init__(self, gdisplay):
		super().__init__()
		self.gdisplay = gdisplay


	def writeToScreen(message, xcoord, ycoord, fontSize):
		font=pygame.font.Font(None,fontSize)
		scoretext=font.render(message, 10,(0,0,0))
		gdisplay.blit(scoretext, (xcoord, ycoord))









