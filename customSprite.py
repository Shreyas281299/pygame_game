import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (450,450)




    def update(self,box_mov,right_mov,movement = None):
        self.rect.centery+=box_mov
        self.rect.centerx +=right_mov

        if movement == 'space':
            self.rect.centery-=5
