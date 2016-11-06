import pygame

class lessonPlan:

	def __init__(self, gdisplay):
		#super().__init__()
		self.gdisplay = gdisplay


	def writeToScreen(self, message, xcoord, ycoord, fontSize, gdisplay):
		#print ("write to screeen g display", gdisplay)
		font=pygame.font.Font(None,fontSize)
		scoretext=font.render(message, 10,(0,0,0))
		gdisplay.blit(scoretext, (xcoord, ycoord))

	def test(self,x,y):
		return









