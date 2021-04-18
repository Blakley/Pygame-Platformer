# script imports
import settings

# library imports
import pygame
from pygame.locals import *


class Player():
	def __init__(self, x, y, screen):
		self.screen = screen

		self.images_right = []
		self.images_left = []
		self.img_index = 0
		self.counter = 0 # animation speed
		self.direction = 0
		
		self.load_assets()
		self.image = self.images_right[self.img_index] # first animation
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.vel_y = 0
		self.jumped = False
		self.crouch = False
		
	# Load all character images
	def load_assets(self):
		for i in range(1, 5):
			# load right player sprite images
			imageR = pygame.image.load(f'../assets/Player/guy{i}.png')
			imageR = pygame.transform.scale(imageR, (40, 80))
			# make left player sprite images
			imageL = pygame.transform.flip(imageR, True, False)
			self.images_right.append(imageR)
			self.images_left.append(imageL)		

	# handle key presses
	def controller(self, dx, dy):
		value = []
		key = pygame.key.get_pressed()
		# w, a, s, d
		if key[pygame.K_w] and self.jumped == False: # jumping
			self.vel_y = -15
			self.jumped = True
		
		if key[pygame.K_w] == False:
			self.jumped = False

		if key[pygame.K_s] and self.crouch == False: # crouching
			self.crouch = True

		if key[pygame.K_s] == False:
			self.crouch = False
		
		if key[pygame.K_a]: # moving left
			dx -= 5
			self.counter += 1
			self.direction = -1 
		
		if key[pygame.K_d]: # moving right
			dx += 5
			self.counter += 1
			self.direction = 1 
		
		if key[pygame.K_a] == False and key[pygame.K_d] == False: # reset sprite animation
			self.counter = 0
			self.img_index = 0
			
			# determine the position of the player after they've stopped moving
			if self.direction == 1:
				self.image = self.images_right[self.img_index]

			if self.direction == -1:
				self.image = self.images_left[self.img_index]

		value.append(dx)
		value.append(dy)
		return value

	# handle player collision
	def collision(self):
		print("")

	# handle sprite animation
	def animation(self, cool_down):
		if self.counter > cool_down:
			self.counter = 0
			self.img_index += 1 # change the animation
			
			if self.img_index >= len(self.images_right): # reset sprite img_index
				self.img_index = 0
			
			if self.direction == 1:
				self.image = self.images_right[self.img_index]
			
			if self.direction == -1:
				self.image = self.images_left[self.img_index]

	# Update the player
	def draw_player(self):
		dx = 0
		dy = 0
		walk_cool_down = 5

		# input handler
		key = self.controller(dx, dy) 
		dx = key[0]
		dy = key[1]
		
		# animation handler
		self.animation(walk_cool_down)

		# add gravity
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		# check for collision
		# self.collision()

		# update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > settings.h:
			self.rect.bottom = settings.h
			dy = 0

		self.screen.blit(self.image, self.rect)

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

class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.w, settings.h))
		pygame.display.set_caption('Mazer') # title
		# icon = pygame.image.load('../assets/icon.png') # icon
		# pygame.display.set_icon(icon)		
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.start()

	# start game
	def start(self):
		world = World(self.screen)
		player = Player(100, settings.h - 130, self.screen)
		
		run = True 
		while(run):
			self.clock.tick(self.fps) 

			world.draw_world()
			world.draw_grid()
			world.draw_tiles()
			player.draw_player()

			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					run = False
			pygame.display.update() 

# begin
game = Game()
pygame.quit()