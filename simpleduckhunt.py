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
 
##====================================================  
class Game:
	
	def __init__(self):
	
		#Give this game a list of players to pick from.
		self.players = {"P1": InteractivePlayer(), "R": Robot()}
		self.player = self.players["P1"]
		
		#Create clock to manage fps.
		self.clock = pygame.time.Clock()
		
		self.ducks = []
		
		self.end = False
		
		self.window = pygame.display.set_mode((info.current_w, info.current_h))
		
		self.makeDucks(3)
	
	def makeDucks(self, how_many):
		for i in range(how_many):
			self.ducks.append(self.createDuck(self.window, "easy"))
	
	def render_Objects(self):
	
		self.window.fill([173,216,230])
	
		for duck in self.ducks:
			duck.beDrawn()
			
		pygame.display.update()
		
		self.clock.tick(20)
	
	
	#receiving shotting location from Player
	def getInputs(self):
	
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				self.end = True
			if(event.type == pygame.MOUSEBUTTONDOWN):
				pass
	
		locationWhereShot = self.player.shotAt()
		isShot = self.check_hit_duck(locationWhereShot)
		
		
	#check if duck is shot
	def check_hit_duck(self, location):
		YELLOW = [250, 250, 0, 255]
		if self.window.get_at(location) == YELLOW:
			return True
		else:
			return False
			
	#update objects	
	def updateObjects(self):
		for duck in self.ducks:
			duck.move()
			
	#Starts the game loop  
	def start(self):
	
		while(not self.quit()):

			self.getInputs()

			self.updateObjects()

			self.render_Objects()

		
	def checkDucksGone(self):
		if(len(self.ducks) <= 0):
			return True
		else:
			return False
		
		
	def quit(self): 
		return self.end
		
	def createDuck(self, window, typeDuck):
	
		if(typeDuck == "hard"):
			return Duck(window, 10)
		elif(typeDuck == "medium"):
			return  Duck(window, 7)
		else:
			return Duck(window, 5)
			
			
			
			
			
			
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
 
 
 
 
 
 
 
 
 
 
 
 
		
	