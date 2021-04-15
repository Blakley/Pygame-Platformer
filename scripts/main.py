# script imports
import settings

# library imports
import pygame
from pygame.locals import *

#
class Player():
	def __init__(self, x, y):
		print("")

	def collision(self):
		print("")

	def draw(self):
		print("")

#
class World():
	def __init__(self, data):
		self.tiles = []

	# draws the world data from the tiles we created
	def draw(self):
		for tile in self.tiles:
			screen.blit(tile[0], tile[1]) # draw the (img, img_rect)

#
class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.w, settings.h))
		pygame.display.set_caption('Mazer')
		self.start()

	def start(self):
		run = True 
		while(run):
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					run = False
		pygame.display.update() 

# 
game = Game()
pygame.quit()


