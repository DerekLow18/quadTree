import pygame
import os
import sys
from platform import Platform

class level1():
    def ground(lvl, x, y, w, h):
        ground_list = pygame.sprite.Group()
        ground = Platform(x, y, w, h, '../images/platform.png')
        ground_list.add(ground)

        return ground_list

    def platform(lvl):
        
        return plat_list