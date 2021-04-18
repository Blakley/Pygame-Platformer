#
class Player():
	def __init__(self, x, y, screen):
		self.images_right = []
		self.images_left = []
		self.img_index = 0
		self.animation_speed = 0

		self.screen = screen
		self.load_assets()

		# first animation
		self.image = self.images_right[self.img_index] 
		self.rect = self.image.get_rect()

		self.x = x # player x pos
		self.y = y # player y pos
		self.vel_y = 0 # player y velocity
		self.jumped = False
		self.player_direction = 0
		self.key = pygame.key.get_pressed() # controller
		
	# load all player assets
	def load_assets(self):
		for i in range(1, 5):
			# load right player sprite images
			imageR = pygame.image.load(f'../assets/Player/guy{i}.png')
			imageR = pygame.transform.scale(imageR, (settings.tile_size + 25, settings.tile_size + 25))
			# make left player sprite images
			imageL = pygame.transform.flip(imageR, True, False)
			self.images_right.append(imageR)
			self.images_left.append(imageL)

	#
	def collision(self):
		print("")

	#
	def controller(self):
		if self.key[pygame.K_w] and self.jumped == False: # jump
			self.vel_y = -15
			self.jumped = True
		
		if self.key[pygame.K_w] == False:
			self.jumped = False	

		if self.key[pygame.K_a]: # left
			dx -= 5
			self.animation_speed += 1
			self.player_direction = -1 
		
		if self.key[pygame.K_d]: # right
			dx += 5
			self.animation_speed += 1
			self.player_direction = -1	

		if self.key[pygame.K_a] == False and self.key[pygame.K_d] == False: # reset animation
			self.animation_speed = 0
			self.img_index = 0
			# determine the position of the player after they've stopped moving
			if self.player_direction == 1:
				self.image = self.images_right[self.index]
			if self.player_direction == -1:
				self.image = self.images_left[self.index]

	#
	def draw_player(self):
		dx = 0
		dy = 0
		walk_cool_down = 0

		# controller handler
		self.controller()

		# gravity check
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		# collision check
		# self.collision()

		# update coordinates
		self.x += dx
		self.y += dy

		# stop player from falling from bottom of screen (temp)
		if self.rect.bottom > settings.h:
			self.rect.bottom = settings.h
			dy = 0

		# draw the player
		self.screen.blit(self.image, self.rect)
