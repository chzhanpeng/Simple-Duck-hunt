#This is the module which will hold game classes and their respective helping classes.

#Import the player classes.
from duckhuntplayers import *

#Import ducks
from ducks import *

#Import mycolors.
import mycolors

#Importing pygame.
import pygame

class Game:
	
	def __init__(self):
	
		#Give this game a list of players to pick from.
		self.players = {"P1": InteractivePlayer(), "R": Robot()}
		self.player = self.players["P1"]
		
		#Create clock to manage fps.
		self.clock = pygame.time.Clock()
		#Create info object for screen resolution and other info.
		self.info = pygame.display.Info()
		
		#Ducks list.
		self.ducks = []
		
		#Flag to keep game going.
		self.end = False
		
		#Window for displaying stuff.
		self.window = pygame.display.set_mode((self.info.current_w, self.info.current_h))
		
		#Create the ducks for this game.
		self.makeDucks(3)
	
	def makeDucks(self, how_many):
		for i in range(how_many):
			self.ducks.append(self.createDuck(self.window, "easy"))
	
	def render_Objects(self):
	
		self.window.fill(mycolors.LIGHT_BLUE)
	
		for duck in self.ducks:
			duck.beDrawn()
			
		pygame.display.update()
		
		self.clock.tick(20)
	
	
	#receiving shotting location from Player
	def getInputs(self):
	
		#Go over events for event handling.
		for event in pygame.event.get():
		
			#Event handling to quit game.
			if(event.type == pygame.QUIT):
				self.end = True
				
			#Mouse event handling.
			if(event.type == pygame.MOUSEBUTTONDOWN):
				pass
	
		locationWhereShot = self.player.shotAt()
		isShot = self.check_hit_duck(locationWhereShot)
		
		
	#check if duck is shot
	def check_hit_duck(self, location):
	
		if self.window.get_at(location) == mycolors.YELLOW:
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
			
			
			
			
			
			
