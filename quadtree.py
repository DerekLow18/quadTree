'''
this will handle the collision detection algorithms using
the quadtree data structure.
'''
import pygame
import collision

displayTree = True

def rect_quad_split(rect):
    w=rect.width/2
    h=rect.height/2
    r1=[]
    r1.append(pygame.Rect(rect.left, rect.top, w,h))
    r1.append(pygame.Rect(rect.left+w,rect.top,w,h))
    r1.append(pygame.Rect(rect.left,rect.top+h,w,h))
    r1.append(pygame.Rect(rect.left+w,rect.top+h,w,h))
    return r1

class quadTree(object):
    def __init__(self,level,rect, entities=[], color=(0,0,0)):
        self.maxlevel = 4
        self.level=level
        self.maxentities = 3
        self.rect = rect
        self.entities = entities
        self.color = color
        self.branches = []

    def get_rect(self):

        return self.rect

    def subdivide(self):
        for rect in rect_quad_split(self.rect):
            branch=quadTree(self.level+1, rect, [], (self.color[0]+30, self.color[1], self.color[2]))
            self.branches.append(branch)
    
    def add_entities(self,entity):
        self.entities.append(entity)

    def subdivide_entities(self):
        for entity in self.entities:
            for branch in self.branches:
                if branch.get_rect().colliderect(entity.get_rect()):
                    branch.add_entities(entity)
    
    def render(self,display):
        pygame.draw.rect(display, self.color, self.rect)

    def test_collisions(self):
        for i, entity in enumerate(self.entities):
            for entity2 in self.entities[i+1:]:
                if pygame.sprite.collide_rect(entity,entity2):
                    print("collision detected")
                    collision.collision(entity, entity2)

    def update(self,display):
        if len(self.entities) > self.maxentities and self.level <=self.maxlevel:
            self.subdivide()
            self.subdivide_entities()
            for branch in self.branches:
                branch.update(display)
        else:
            self.test_collisions()
            if displayTree:
                self.render(display)