import mycolors
import pygame

class HUD:

	def __init__(self, window):
		self.window = window
		self.width = window.get_width()
		self.height = window.get_height()
		
	def msg_to_screen(msg, color, where):
		font = pygame.font.SysFront(None, 25)
		screen_text = font.render(msg, True, color)
		self.window.blit(screen_text, where)
		
	def drawBullet(self):
		self.window.fill(mycolors.BLACK , rect=[self.width * 0.1, self.height * 0.9, self.width * 0.1, self.height * 0.05])	
		self.msg_to_screen("SHOT", mycolors.light_blue, [self.width*0.1, self.height*0.95])
		gray = (120, 112, 140,255)
		self.window.fill(gray, rect=[self.width *0.11, self.height * 0.91, self.width *0.02,self.width *0.02])
