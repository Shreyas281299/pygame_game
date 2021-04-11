import pygame
import sys
import random
import time
from customSprite import Player
from customSprite import obs


pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()

bg = pygame.image.load('bg.jpeg')
bg_2 =pygame.image.load('bg.jpeg') 



box = Player()
mov_sprite = pygame.sprite.Group()
mov_sprite.add(box)
obs_sprite = pygame.sprite.Group()

spawn_obst = pygame.USEREVENT
pygame.time.set_timer(spawn_obst,2500)


x = 0
y1 = 0
y2 = -900
grav = 0.2
box_mov = 0
right_mov = 0
direction = 'right'
bg_mov = 5
box_mov = 0
obs_mov = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == spawn_obst:
            met = obs()
            obs_sprite.add(met)



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                if box.rect.centerx < 330 or box.rect.centerx > 570:
                    if box.rect.centerx < 330 :
                        box.rect.centerx = 300
                        y1  -= 2*bg_mov
                        y2  -= 2*bg_mov
                        box_mov = 5
                        right_mov = 0
                    if box.rect.centerx > 570:
                        box.rect.centerx = 600
                        y1  -= 2*bg_mov
                        y2  -= 2*bg_mov
                        box_mov = 5
                        right_mov = 0

            if event.key == pygame.K_SPACE:
                box_mov = -3
                if direction == 'left':
                    right_mov += -3
                elif direction == 'right':
                    right_mov += 3
                elif direction == 'up':
                    box_mov += 3

                mov_sprite.update(box_mov,right_mov,direction,'space')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if direction == 'left':
                    direction = 'up'
                else:
                    direction = 'right'
                mov_sprite.update(box_mov,right_mov,direction,'right')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if direction =='right':
                    direction = 'up'
                else:
                    direction = 'left'
                mov_sprite.update(box_mov,right_mov,direction,'left')

        
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

    y1 +=bg_mov
    y2 += bg_mov
    if y1 >900 :
       y1 = 0
       y2 = -900

    pygame.display.update()

    screen.blit(bg,(x,y1))
    screen.blit(bg_2,(x,y2))

    mov_sprite.draw(screen) 
    obs_sprite.draw(screen)

    for sprite in obs_sprite:
        if sprite.rect.centery > 700:
            obs_sprite.remove(sprite)

    mov_sprite.update(box_mov,right_mov,direction)
    obs_sprite.update(obs_mov)
    clock.tick(200)


