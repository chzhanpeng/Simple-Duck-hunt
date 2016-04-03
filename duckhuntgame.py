#This is the module which will hold game classes and their respective helping classes.

#Import the player classes.
from duckhuntplayers import *
#Import ducks
from ducks import *

#Importing pygame.
import pygame

class Game:
	
	def __init__(self, info):
	
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
			
			
			
			
			
			
