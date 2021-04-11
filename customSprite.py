import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (450,450)

    def update(self,box_mov,right_mov,direction,movement = None):
        self.rect.centery+=box_mov
        self.rect.centerx +=right_mov
        if movement == 'space':
            self.rect.centery-=5
     

class obs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        i = random.randint(1,7)
        self.image = pygame.Surface((7,7))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self. image = pygame.transform.rotate(self.image,random.randint(-180,180))
        self.rect.center = (random.randint(310,590),-5)
    

    
    def update(self,grav):
        self.rect.centery +=grav
