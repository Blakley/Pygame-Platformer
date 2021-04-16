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
	def __init__(self, screen):
		self.tiles = []
		self.load_assets()
		self.screen = screen
		self.setup_data()

	# loads all the game assets
	def load_assets(self):
		# load then update the background scale
		self.bg1 = pygame.image.load(settings.imgT[0])
		self.bg1 = pygame.transform.scale(self.bg1, (settings.w, settings.h)) 
		self.sun = pygame.image.load(settings.imgT[1]) # load sun
		self.dirt = pygame.image.load(settings.imgT[4]) # load dirt


	# setup images and tile data
	def setup_data(self):
		row = 0
		for r in settings.data:
			col = 0
			for tile in r:
				if (tile == 1): # grass_tile ID
					img = pygame.transform.scale(self.dirt, (settings.tile_size, settings.tile_size))
					img_rect = img.get_rect()
					img_rect.x = col * settings.tile_size
					img_rect.y = row * settings.tile_size
					tile = (img, img_rect)
					self.tiles.append(tile)
				col += 1
			row += 1

	# Test grid
	def draw_grid(self):
		for line in range(0, 20):
			pygame.draw.line(self.screen, (255, 255, 255), (0, line * settings.tile_size), (settings.w, line * settings.tile_size))
			pygame.draw.line(self.screen, (255, 255, 255), (line * settings.tile_size, 0), (line * settings.tile_size, settings.h))

	# draw the world assets
	def draw_world(self):
		self.screen.blit(self.bg1, (0, 0))
		self.screen.blit(self.sun, (100, 100))

	# draws the world data from the tiles we created
	def draw(self):
		for tile in self.tiles:
			self.screen.blit(tile[0], tile[1]) # draw the (img, img_rect)

#
class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.w, settings.h))
		pygame.display.set_caption('Mazer') # title
		# icon = pygame.image.load('../assets/icon.png') # icon
		# pygame.display.set_icon(icon)
		self.start()

	def start(self):
		world = World(self.screen)
		run = True 
		while(run):
			# draw game content
			world.draw_world()
			world.draw_grid()
			world.draw()
			
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					run = False
			pygame.display.update() 

# 
game = Game()
pygame.quit()


