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

pygame.mixer.music.load

class sfx:

	def __init__(self):
		pass
	
######################################################  
game = Game(info)
game.start()

#End pygame
pygame.quit()
quit()
 
 
 
 
 
 
 
 
 
 
 
 
		
	
