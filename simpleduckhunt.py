#Import the gaming library: pygame
import pygame

#Initialize pygame objects.
pygame.init()

##====================================================
#Color definitions.

YELLOW = (255, 255, 0, 255)

##====================================================

info = pygame.display.Info()

##====================================================
class Player(object):
	
	#Player class constructor
	def __init__(self):
		
		#Initializes score to zero.
		self.score = 0
		self.name = "P"
	
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
	def shotAt(self):
		return (0,0)
		
	def update_score(self, points):
		self.score += points
		
	def update(self):
		pass
		
	def getName(self):
		pass
		
	def __eq__(self , other):
		self.name == other.name

##====================================================

##====================================================
class InteractivePlayer(Player):
	
	#Player class constructor
	def __init__(self):
		Player.__init__(self)
		self.name = "P1"
		
	#Returns a 2-tuple with the location at which
	#the player shot at the screen.
		
	def update(self):
		pass
		
	def getName(self):
		return self.name

##====================================================

##====================================================
#Class that represents the robot that will play as this game's player.
class Robot(Player):
	
	def __init__(self):
		Player.__init__(self)
		self.name = "R"
		
	def shotAt(self):
		return (0,0)
		
	def update():
		pass
		
##====================================================

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
 
 
 
 
 
 
 
 
 
 
 
 
		
	
