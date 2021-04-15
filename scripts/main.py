import pygame
from pygame.locals import *

#
def initialize_screen():	
	pygame.init()

	screen_width = 1000;
	screen_height = 1000;

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Mazer')

	run_game()


def run_game():
	run = True 
	while(run):
		for event in pygame.event.get(): # loop through the events 
			if event.type == pygame.QUIT: # if the event is quit, exit game
				run = False
	pygame.display.update() # update our screen


pygame.quit()

if __name__ == '__main__':
	initialize_screen()