#Import the gaming library: pygame
import pygame

#Import all classes from the duckhuntgame module
from duckhuntgame import *

#Initialize pygame objects.
pygame.init()

##====================================================
#Color definitions.

YELLOW = (255, 255, 0, 255)

##====================================================

info = pygame.display.Info()

######################################################		   
class Duck:
	
	def __init__(self, window, speed):
		self.x = 0
		self.y = 0
		
		self.width = info.current_w//10
		self.height = self.width
		
		self.speed = speed
		
		self.window = window
		
		self.color = YELLOW
	#draw duck  
	def beDrawn(self):
		self.window.fill(self.color, rect = [self.x-self.width//2, self.y-self.height//2, self.width, self.height])
		
	#when duck dies
	def die(self):
		self.color = [255, 0, 0]
		
	#check if duck is on screen	
	def onScreen(self):
		width, height = self.window.get_size()		
		return True
			
	
		
	def move(self):
		self.x += self.speed
		
	def changeSpeed(self, speed):
		self.speed = speed
		
######################################################	   

pygame.mixer.music.load

class sfx:

	def __init__(self):
		pass
	
######################################################  
game = Game()
game.start()

#End pygame
pygame.quit()
quit()
 
 
 
 
 
 
 
 
 
 
 
 
		
	
