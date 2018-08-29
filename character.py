#player character class
import pygame
import os

#animation frames
ani=4
class Player(pygame.sprite.Sprite):
	'''
	Spawn a player
	'''
	ALPHA=(255,0,255)
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images= []
		for i in range(1,9):
			img = pygame.image.load(os.path.join('images/walking','hero' + str(i) + '.png')).convert()
			img.convert_alpha()     # optimise alpha
			img.set_colorkey(self.ALPHA) # set alpha so background of sprite does not appear
			self.images.append(img)
			self.image = self.images[0]
			self.rect  = self.image.get_rect()
		self.movex = 0
		self.movey = 0
		self.frame = 0

	def control(self,x,y):
		self.movex += x
		self.movey += y

	def update(self):
		self.rect.x = self.rect.x + self.movex  
		self.rect.y = self.rect.y + self.movey
		if self.movex < 0 or self.movey < 0:
			self.frame += 1
			if self.frame > 3*ani:
				self.frame = 0
			self.image = self.images[self.frame//ani]

		# moving right
		if self.movex > 0 or self.movey > 0:
			self.frame += 1
			if self.frame > 3*ani:
				self.frame = 0
			self.image = self.images[(self.frame//ani)+4]