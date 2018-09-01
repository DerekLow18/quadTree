import pygame
import sys
import os

class Platform(pygame.sprite.Sprite):
    def __init__(self,xloc,yloc,imgw,imgh,img):
        pygame.sprite.Sprite.__init__(self)
        #turn an image into a pygame image object
        self.image=pygame.image.load(os.path.join('images',img)).convert()
        self.image.convert_alpha()
        #self.image.set_colorkey(ALPHA)
        self.rect=self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

        