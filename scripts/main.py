# ------------ imports ------------
import Config
import Levels

import random
import pygame
from pygame.locals import *
from pygame import mixer

# ------------ Globals ------------

# dimensions: 18 x 20
screen_width = 1000 			# screen width
screen_height = 900 			# screen height
tile_size = 50
world_tiles = []				# first layer

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mazer')

in_menu = True
game_finished = False
game_over = 0 					# Game-Over flag
current_level = 0				# level counter
max_levels = 3					# number of game levels (0 indexed)
score_count = 0					# coin score count

	# --> Sounds
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

sounds = []
menu_sound = False
game_sound = False

plats = []			# group of platforms
check_points = []	# group of checkpoints
lava_tiles = []		# group of lava tiles

# -----------------------------------------------------------------------------------------------------------

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		# draw button
		screen.blit(self.image, self.rect)

		return action

# -----------------------------------------------------------------------------------------------------------

class CheckPoint(pygame.sprite.Sprite):
	def __init__(self, x, y, screen):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["sign"])
		self.image = pygame.transform.scale(img, (int(tile_size // 1.3), int(tile_size // 1.3)) )
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y + 63 # adjust the height to go ontop of grass

# -----------------------------------------------------------------------------------------------------------

class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y, screen):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["lava"])
		self.image = pygame.transform.scale(img, (tile_size, tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

# -----------------------------------------------------------------------------------------------------------

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, move_x, move_y, screen):
		self.screen = screen
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load(Config.Sprites["ground_2"])
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.move_direction = 1
		self.move_counter = random.randint(0, 40)

		self.move_x = move_x # flag to move in x direction
		self.move_y = move_y # flag to move in y direction

	# handle platform movement
	def update(self):
		self.rect.x += self.move_direction * self.move_x
		self.rect.y += self.move_direction * self.move_y
		self.move_counter += 1

		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1

# -----------------------------------------------------------------------------------------------------------

class World():
	def __init__(self):
		self.assets = {}
		self.load_assets()
		self.initialize_tiles()

	# Load game assets
	def load_assets(self):
		# Load the background
		self.background = pygame.image.load(Config.Sprites["background"])
		self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

		# Create an asset dictionary
		for name, path in Config.Sprites.items():
			if name != "background":
				self.assets[name] =  pygame.image.load(path)

	# Makes an image game object
	def create_tile(self, row, col, name, custom_size, custom_location):
		global tile_size
		global world_tiles

		# default size
		if not custom_size:

			img = pygame.transform.scale(self.assets[name], (tile_size, tile_size))
			img_rect = img.get_rect()

			if not custom_location:
				img_rect.x = col * tile_size
				img_rect.y = row * tile_size
				t = (img, img_rect)
				world_tiles.append(t)
			else:
				img_rect.x = custom_location[0]
				img_rect.y = custom_location[1]
				t = (img, img_rect)
				world_tiles.append(t)

		else:
			img = pygame.transform.scale(self.assets[name], (custom_size[0], custom_size[1]))
			img_rect = img.get_rect()

			if not custom_location:
				img_rect.x = col * tile_size
				img_rect.y = row * tile_size
				t = (img, img_rect)
				world_tiles.append(t)
			else:
				img_rect.x = custom_location[0]
				img_rect.y = custom_location[1]
				t = (img, img_rect)
				world_tiles.append(t)

	# Initialize game tiles
	def initialize_tiles(self):
		global platforms
		global check_points
		global environmentals
		global world_tiles
		global current_level

		world_tiles = []

		row = 0
		index = 0
		for r in Levels.level[current_level]:
			col = 0
			for tile in r:
				if (tile == 1):
					self.create_tile(row, col, "ground_1", False, False)

				if (tile == 2):
					self.create_tile(row, col, "ground_2", False, False)

				if (tile == 2.1):	# moving platform (Horizontal)
					platform = Platform(col * tile_size, row * tile_size , 1, 0, screen)
					plats[0].add(platform)

				if (tile == 2.2):	# moving platform (Vertical)
					platform = Platform(col * tile_size, row * tile_size , 0, 1, screen)
					plats[0].add(platform)

				if (tile == 3):
					self.create_tile(row, col, "ground_3", False, False)

				if (tile == 4):
					self.create_tile(row, col, "ground_4", False, False)

				if (tile == 5):
					self.create_tile(row, col, "ground_5", False, False)

				if (tile == 6):
					self.create_tile(row, col, "ground_6", False, False)

				if (tile == 7):
					self.create_tile(row, col, "ground_7", False, False)

				if (tile == 8):
					self.create_tile(row, col, "ground_8", False, False)

				if (tile == 9):
					self.create_tile(row, col, "ground_9", False, False)

				if (tile == 10):
					self.create_tile(row, col, "ground_10", False, False)

				if (tile == 11):
					self.create_tile(row, col, "ground_11", False, False)

				if (tile == 12):
					location = []
					location.append(col * tile_size)
					location.append(row * tile_size + 50)
					self.create_tile(row, col, "grass_1", False, location)

				if (tile == 13):
					location = []
					location.append(col * tile_size)
					location.append(row * tile_size + 50)
					self.create_tile(row, col, "grass_2", False, location)

				if (tile == 14):
					location = []
					location.append(col * tile_size)
					location.append(row * tile_size + 50)
					self.create_tile(row, col, "grass_3", False, location)

				if (tile == 15):
					location = []
					location.append(col * tile_size)
					location.append(row * tile_size + 50)
					self.create_tile(row, col, "grass_4", False, location)

				if (tile == 16):
					location = []
					location.append(col * tile_size)
					location.append(row * tile_size + 50)
					self.create_tile(row, col, "grass_5", False, location)

				if (tile == 17):
					self.create_tile(row, col, "bush_1", False, False)

				if (tile == 18):
					self.create_tile(row, col, "bush_2", False, False)

				if (tile == 19):
					self.create_tile(row, col, "tree_1", False, False)

				if (tile == 20):
					self.create_tile(row, col, "tree_2", False, False)

				if (tile == 21):
					self.create_tile(row, col, "rock_1", False, False)

				if (tile == 22):
					self.create_tile(row, col, "rock_2", False, False)

				if (tile == 23):
					check = CheckPoint(col * tile_size, row * tile_size, screen)
					check_points[0].add(check)

				if (tile == 24):
					lava = Lava(col * tile_size, row * tile_size, screen)
					lava_tiles[0].add(lava)

				index += 1
				col += 1
			row += 1

		# reverse the list so assets are drawn from bottom to top
		world_tiles = [ele for ele in reversed(world_tiles)]

	# Draw the background
	def draw_world(self):
		screen.blit(self.background, (0, 0))

	# Draw the world data from the tiles we created
	def draw_tiles(self):
		if world_tiles:
			for tile in world_tiles:
				screen.blit(tile[0], tile[1])

# -----------------------------------------------------------------------------------------------------------

class Character():
	def __init__(self, x, y):
		# images
		self.idle_right = []
		self.idle_left = []

		self.run_right = []
		self.run_left = []

		self.death_right = []
		self.death_left = []

		self.jump_right = []
		self.jump_left = []

		self.img_index = 0 # current frame
		self.counter = 0 # animation speed
		self.death_counter = 0

		# load assets
		self.load_assets()
		self.image = self.idle_right[self.img_index] # first frame

		# coordinates
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.w = self.image.get_width()
		self.rect.h = self.image.get_height()

		self.direction = 0
		self.vel_y = 0
		self.jumped = False
		self.in_air = False

		self.animation = "idle"
		self.cool_down = 10 # wait 10 frames before next img animation

	# Load all character images
	def load_assets(self):
		for name, path in Config.Player.items():
			img = pygame.image.load(path)
			img = pygame.transform.scale(img, (tile_size, tile_size))
			img_left = pygame.transform.flip(img, True, False)

			if 'idle' in name:
				self.idle_right.append(img)
				self.idle_left.append(img_left)

			if 'run' in name:
				self.run_right.append(img)
				self.run_left.append(img_left)

			if 'fall' in name:
				self.fall_right.append(img)
				self.fall_left.append(img_left)

			if 'death' in name:
				self.death_right.append(img)
				self.death_left.append(img_left)

			if 'jump' in name:
				self.jump_right.append(img)
				self.jump_left.append(img_left)

	# handle idle animation
	def idle_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.idle_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.idle_right[self.img_index]

		if self.direction == -1:
			self.image = self.idle_left[self.img_index]

	# handle jump animation
	def jump_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.jump_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.jump_right[self.img_index]

		if self.direction == -1:
			self.image = self.jump_left[self.img_index]

	# handle running animation
	def run_animation(self):
		if self.counter > self.cool_down:
			self.img_index += 1
			self.counter = 0

		if self.img_index >= len(self.run_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.run_right[self.img_index]

		if self.direction == -1:
			self.image = self.run_left[self.img_index]

	# handle death animation
	def death_animation(self):
		global game_over

		if self.death_counter > self.cool_down + 1:
			self.death_counter = 0
			game_over = -1
		else:
			self.img_index += 1

		if self.img_index >= len(self.death_right):
			self.img_index = 0

		if self.direction == 1 or self.direction == 0:
			self.image = self.death_right[self.img_index]

		if self.direction == -1:
			self.image = self.death_left[self.img_index]

		self.death_counter += 1


	# handle key presses
	def controller(self, dx, dy):
		global sounds

		value = []
		key = pygame.key.get_pressed()

		# currently idle
		if not key[pygame.K_w] or not key[pygame.K_a] or not key[pygame.K_d]:
			self.counter += 1
			self.animation = "idle"

		# currently jumping
		if key[pygame.K_w] and self.jumped == False and self.in_air == False:
			self.vel_y = -14 # jump height
			self.jumped = True
			self.counter += 1
			self.animation = "jump"
			sounds[1].play()

		if key[pygame.K_w] == False:
			self.jumped = False

		# currently running right
		if key[pygame.K_d]:
			dx += 5
			self.counter += 1
			self.direction = 1
			self.animation = "run"

		# currently running left
		if key[pygame.K_a]:
			dx -= 5
			self.counter += 1
			self.direction = -1
			self.animation = "run"

		value.append(dx)
		value.append(dy)
		return value

	# handle player collision
	def collision(self, dx, dy):
		global plats
		global check_points
		global lava_tiles
		global game_over
		global world_tiles
		global game_finished
		global current_level
		global max_levels

		values = []
		collision_thresh = 20 # distance between moving platform in y dir

		self.in_air = True
		for tile in world_tiles:
			# check for collision in x direction ...
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.w, self.rect.h):
				dx = 0 # if we collide, stop player

			# check collision in y direction of expected dy (change in y)
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.w, self.rect.h):
				# check if jumping
				if self.vel_y < 0:
					self.vel_y = 0
					dy = tile[1].bottom - self.rect.top # dist between top of player and bottom of block

				# check if falling
				elif self.vel_y >= 0:
					self.vel_y = 0
					self.in_air = False
					dy = tile[1].top - self.rect.bottom

		# check for collision with platforms
		for platform in plats[0]:
			# check for x collision using expected position (dx) value
			if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.w, self.rect.h):
				dx = 0
			# check for y collision
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.w, self.rect.h):
				# check if below platform
				if abs((self.rect.top + dy) - platform.rect.bottom) < collision_thresh:
					self.vel_y = 0
					dy = platform.rect.bottom - self.rect.top
				# check if above platform
				elif abs((self.rect.bottom + dy) - platform.rect.top) < collision_thresh:
					self.rect.bottom = platform.rect.top - 1
					self.in_air = False
					dy = 0
				# move sideways with the platform
				if platform.move_x != 0:
					self.rect.x += platform.move_direction

		# check for collision with checkpoint
		if pygame.sprite.spritecollide(self, check_points[0], False):
			if current_level + 1 > max_levels:
				game_finished = True
				game_over = 0
			else:
				game_over = 1

		# check for collision with lava
		if pygame.sprite.spritecollide(self, lava_tiles[0], False):
			self.death_animation()
			self.rect.y = self.rect.y
			self.rect.x = self.rect.x

		values.append(dx)
		values.append(dy)
		return values

	# create a 2px rect outline around the player
	def draw_outline(self):
		pygame.draw.rect(screen, (179, 29, 18), self.rect, 2)

	# handle the player
	def draw_player(self):
		global game_over
		dx = 0
		dy = 0

		if game_over == 0:
			# input handler
			key = self.controller(dx, dy)
			dx = key[0]
			dy = key[1]

			# animation handling
			if self.animation == "idle":
				self.idle_animation()

			if self.animation == "jump":
				self.jump_animation()

			if self.animation == "run":
				self.run_animation()

			# add gravity
			self.vel_y += 1
			if self.vel_y > 10:
				self.vel_y = 10
			dy += self.vel_y

			# check for collision
			col = self.collision(dx, dy)
			dx = col[0]
			dy = col[1]

			# handle out of bounds
			if self.rect.x + dx >= -25 and self.rect.x + dx <= 977:
				self.rect.x += dx

			if self.rect.y + dy >= 1000:
				game_over = -1
			else:
				self.rect.y += dy

		screen.blit(self.image, self.rect)

# -----------------------------------------------------------------------------------------------------------

class Game():
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 512)
		mixer.init()
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.game_menu()
		self.start()

	# setup in-game menu
	def game_menu(self):
		play_img = pygame.image.load(Config.UI["play"])
		quit_img = pygame.image.load(Config.UI["quit"])
		continue_img = pygame.image.load(Config.UI["continue"])
		resume_img = pygame.image.load(Config.UI["resume"])

		play_img = pygame.transform.scale(play_img, (200, 70))
		quit_img = pygame.transform.scale(quit_img, (200, 70))
		continue_img = pygame.transform.scale(continue_img, (200, 70))
		resume_img = pygame.transform.scale(resume_img, (200, 70))

		self.play_button = Button(screen_width // 2 - 100, screen_height // 2, play_img)
		self.quit_button = Button(screen_width // 2 - 100, screen_height // 2 + 110, quit_img)
		self.continue_button = Button(screen_width // 2 - 100, screen_height // 2, continue_img)
		self.resume_button = Button(screen_width // 2 - 100, screen_height // 2, resume_img)

	# load sounds
	def sounds(self):
		global sounds

		theme_fx = pygame.mixer.Sound(Config.Sounds["theme"])
		theme_fx.set_volume(0.5)

		jump_fx = pygame.mixer.Sound(Config.Sounds["jump"])
		jump_fx.set_volume(0.5)

		over_fx = pygame.mixer.Sound(Config.Sounds["over"])
		over_fx.set_volume(0.5)

		complete_fx = pygame.mixer.Sound(Config.Sounds["complete"])
		complete_fx.set_volume(0.5)

		sounds.append(theme_fx)
		sounds.append(jump_fx)
		sounds.append(over_fx)
		sounds.append(complete_fx)

		sounds[0].play(-1) # loop game theme

	# resets platform group
	def reset_groups(self):
		global plats
		global check_points
		global lava_tiles

		plats = []
		check_points = []
		lava_tiles = []

		self.plat_group.empty()
		self.check_group.empty()
		self.lava_group.empty()

	# create all properties
	def properties(self):
		global plats
		global check_points
		global lava_tiles

		self.plat_group = pygame.sprite.Group()
		self.check_group = pygame.sprite.Group()
		self.lava_group = pygame.sprite.Group()

		plats.append(self.plat_group)
		check_points.append(self.check_group)
		lava_tiles.append(self.lava_group)

	# load level
	def load_level(self):
		global game_over

		self.reset_groups()
		self.properties()
		world = World()
		player = Character(0, screen_height - 130)
		game_over = 0

		values = []
		values.append(player)
		values.append(world)
		return values

	# handle level timer
	def game_timer(self):
		global current_level
		timer = 30
		ttext = str(timer)

		self.timer_counter, self.timer_text = timer, ttext.rjust(3)
		pygame.time.set_timer(pygame.USEREVENT, 1000)
		self.timer_font = pygame.font.SysFont('comicsansms', 25)

	# start game functionality
	def start(self):
		global in_menu
		global game_over
		global game_finished
		global max_levels
		global current_level

		self.sounds()
		self.properties()
		world = World()
		player = Character(0, screen_height - 130)
		self.game_timer()

		run = True
		while(run):
			self.clock.tick(self.fps)

			# draw assets onto the screen
			world.draw_world()

			# setup main menu
			if in_menu:
				if self.quit_button.draw():
					run = False
				if self.play_button.draw():
					in_menu = False
			else:
				world.draw_tiles()
				check_points[0].draw(screen)
				lava_tiles[0].draw(screen)
				player.draw_player()

				# player active
				if game_over == 0:
					plats[0].update()

				# player finished level
				if game_over == 1:
					self.timer_counter = 0
					current_level += 1
					values = self.load_level()
					player = values[0]
					world = values[1]

					if current_level == max_levels:
						game_finished = True
					else:
						self.game_timer()
				# player death
				if game_over == -1:
					self.timer_counter = 0
					if self.resume_button.draw():
						values = self.load_level()
						player = values[0]
						world = values[1]
						self.game_timer()
					if self.quit_button.draw():
						run = False

				# player won
				if game_finished:
					self.timer_counter = 0
					if self.quit_button.draw():
						run = False

				plats[0].draw(screen)
				screen.blit(self.timer_font.render(self.timer_text, True, (47, 48, 29)), (60, 42))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				# game timer
				if event.type == pygame.USEREVENT:
					self.timer_counter -= 1
					if self.timer_counter > 0:
						self.timer_text = str(self.timer_counter).rjust(3)
					else:
						# player ran out of time
						self.timer_text = '0'.rjust(3)
						if not game_finished:
							game_over = -1

			pygame.display.update()

# Start the game
game = Game()
pygame.quit()
