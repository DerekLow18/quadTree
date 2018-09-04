'''
Collision detection algorithms
'''

def collision(entity1, entity2):
    '''
    basic collision detection
    If the entity was moving left, or if the X was negative,
    then we place it to the right. If it was moving to the right,
    we position it to the right. Same goes for the top.
    '''

    if entity1.movex > 0:
        entity1.rect.right = entity2.rect.left
    elif entity1.movex < 0:
        entity1.rect.left = entity2.rect.right
    elif entity1.movey > 0:
        entity1.rect.bottom = entity2.rect.top - entity1.rect.height/4