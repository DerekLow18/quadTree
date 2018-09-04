import pygame
import os
import sys

sys.path.insert(0,'./levels/')

#import other python scripts
import character
import platform
import level1
import quadtree
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
#level setup
ground_list=level1.level1.ground(1,0,worldy-97, 1080,97)
#plat_list = Level.platform(1)
steps = 10 #how many pixels per movement

#combine all spites into a single group
game_objects = pygame.sprite.Group()
game_objects.add(player_list)
game_objects.add(ground_list)
'''
Main Loop
'''
while main == True:
	#refresh games internal clock based on frame rate
	world.blit(backdrop, backdropbox)
	player.update()
	player_list.draw(world)
	ground_list.draw(world)
	#plat_list.draw(world)
	pygame.display.flip()
	clock.tick(fps)

	pressed_left = False
	pressed_right=False
	pressed_up=False
	pressed_down=False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit()
			main = False
		#initiates movement in some direction
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				pressed_left = True
				#player.control(-steps,0)
			elif event.key == pygame.K_RIGHT or event.key == ord('d'):
				pressed_right=True
				#player.control(steps,0)
			elif event.key == pygame.K_UP or event.key == ord('w'):
				pressed_up=True
				#player.control(0, -steps)
			elif event.key == pygame.K_DOWN or event.key == ord('s'):
				pressed_down=True
				#player.control(0, steps)

		#ends movement in that direction
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				pressed_left=False
				player.control(steps,0)
			elif event.key == pygame.K_RIGHT or event.key == ord('d'):
				pressed_right=False
				player.control(-steps,0)
			elif event.key == pygame.K_UP or event.key == ord('w'):
				pressed_up=False
				player.control(0, steps)
			elif event.key == pygame.K_DOWN or event.key == ord('s'):
				pressed_down=False
				player.control(0, -steps)
			elif event.key == ord('q'):
				pygame.quit()
				sys.exit()
				main = False
	if pressed_left:
		player.control(-steps,0)
	if pressed_right:
		player.control(steps,0)
	if pressed_up:
		player.control(0, -steps)
	if pressed_down:
		player.control(0,steps)
	tree = quadtree.quadTree(0,pygame.Rect(0,0,worldx,worldy), game_objects.sprites())
	tree.update(world)