import pygame
import sys
import random
import time
from customSprite import Player


pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()

bg = pygame.image.load('bg.jpeg')
bg_2 =pygame.image.load('bg.jpeg') 
x = 0
y1 = 0
y2 = -900
box_mov = 0
box = Player()
mov_sprite = pygame.sprite.Group()
mov_sprite.add(box)

grav = 0.2
box_mov = 0
right_mov = 0
direction = 0


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                print(box.rect.centerx)
                box_mov = -3
                if direction == 'left':
                    right_mov += -3
                elif direction == 'right':
                    right_mov += 3
                elif direction == 'up':
                    box_mov += 3

                mov_sprite.update(box_mov,right_mov,'space')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if direction == 'left':
                    direction = 'up'
                else:
                    direction = 'right'
                mov_sprite.update(box_mov,right_mov,'right')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if direction =='right':
                    direction = 'up'
                else:
                    direction = 'left'
                mov_sprite.update(box_mov,right_mov,'left')

        
    if box.rect.centery > 800:
        if right_mov > 0:
            right_mov = right_mov*0.5
        elif right_mov < 0:
            right_mov = right_mov*0.5 

        
        box_mov = -box_mov*0.5



    if box.rect.centerx >= 600 :
        direction = 'left'
        box.rect.centerx-=1
        right_mov = -right_mov*0.8
        box_mov = box_mov*0.8

    elif box.rect.centerx <= 300:
        direction ='right'
        box.rect.centerx+=1
        right_mov = -right_mov*0.8
        box_mov = box_mov*0.8

    box_mov +=grav

    y1 +=5
    y2 += 5
    if y1 >900 :
       y1 = 0
       y2 = -900

    pygame.display.update()
    screen.blit(bg,(x,y1))
    screen.blit(bg_2,(x,y2))
    mov_sprite.draw(screen)
    
    mov_sprite.update(box_mov,right_mov)
    clock.tick(200)


