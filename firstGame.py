import pygame
import os
import sys

#import other python scripts
import character
'''
Setup
'''
#setting the window parameters
worldx = 960
worldy = 500

#fps and animation rate
fps=40
ani=4
#set the clock
clock = pygame.time.Clock()
#initialize the pygame module
pygame.init()

#define the world size
world = pygame.display.set_mode([worldx,worldy])
#load the background image
backdrop = pygame.image.load(os.path.join('./images/background0.png'))
backdropbox=world.get_rect()
#used to close game
main = True

#character setup
player = character.Player()   # spawn player
player.rect.x = 100   # go to x
player.rect.y = 100   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #how many pixels per movement
'''
Main Loop
'''
while main == True:
	#refresh games internal clock based on frame rate
	world.blit(backdrop, backdropbox)
	player.update()
	player_list.draw(world)
	pygame.display.flip()
	clock.tick(fps)
	#exit commands
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit()
			main = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				player.control(-steps,0)
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				player.control(steps,0)
			if event.key == pygame.K_UP or event.key == ord('w'):
				print('jump')

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				player.control(steps,0)
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				player.control(-steps,0)
			if event.key == ord('q'):
				pygame.quit()
				sys.exit()
				main = False