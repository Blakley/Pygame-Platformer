# script imports
import settings

# library imports
import pygame
from pygame.locals import *

#
class Player():
	def __init__(self, x, y, screen):
		self.load_assets()
		self.screen = screen
		self.x = x
		self.y = y
		self.vel_y = 0
		self.jumped = False

	# load all player assets
	def load_assets(self):
		self.p1 = pygame.image.load(settings.imgP[0])
		self.p1 = pygame.transform.scale(self.p1, (settings.tile_size + 25, settings.tile_size + 25))
		self.rect = self.p1.get_rect()

	def collision(self):
		print("")

	def draw_player(self):
		dx = 0 # smooth movement
		dy = 0

		# controller handler
		key = pygame.key.get_pressed()
		if key[pygame.K_a]: # left
			dx -= 5
		if key[pygame.K_d]: # right
			dx += 5
		if key[pygame.K_w] and self.jumped == False: # jump
			self.vel_y = -15
			self.jumped = True
		if key[pygame.K_w] == False:
			self.jumped = False

		# gravity check
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		# collision check

		# update coordinates
		self.x += dx
		self.y += dy

		# stop player from falling from bottom of screen (temp)
		if self.rect.bottom > settings.h:
			self.rect.bottom = settings.h
			dy = 0

		self.screen.blit(self.p1, (self.x, self.y))
		# self.screen.blit(self.p1, self.rect)


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
		self.grassMid = pygame.image.load(settings.imgT[19]) # mid grass asset

	# setup images and tile data
	def setup_data(self):
		row = 0
		for r in settings.data:
			col = 0
			for tile in r:
				if (tile == 1): # grass ID
					img = pygame.transform.scale(self.grassMid, (settings.tile_size, settings.tile_size))
					img_rect = img.get_rect()
					img_rect.x = col * settings.tile_size
					img_rect.y = row * settings.tile_size
					tile = (img, img_rect)
					self.tiles.append(tile)
				if (tile == 2): # dirt ID
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
		self.screen.blit(self.sun, (50, 50))

	# draws the world data from the tiles we created
	def draw_tiles(self):
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
		player = Player(0, 680, self.screen)
		run = True 
		while(run):
			# draw game content
			world.draw_world()
			world.draw_grid()
			world.draw_tiles()
			player.draw_player()
			
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					run = False
			pygame.display.update() 

# 
game = Game()
pygame.quit()


