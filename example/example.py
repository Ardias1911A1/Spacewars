import pygame
from pygame.locals import *

RESOLUTION = (1024 , 768)
pygame.init()

mainWindow = pygame.display.set_mode(RESOLUTION)

background = pygame.image.load("maxresdefault.jpg").convert()
mainWindow.blit(background, (0,0))

character = pygame.image.load("Eisenhorn.jpg").convert()
characterPosition = character.get_rect()
mainWindow.blit(character, characterPosition)

pygame.display.flip()

pygame.key.set_repeat(400, 30)
running = 1
while(running):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                characterPosition.move_ip(0,-3)
                print("w")
            elif event.key == K_s:
                characterPosition.move_ip(0,3)
                print("s")
            elif event.key == K_a:
                characterPosition.move_ip(-3,0)
                print("a")
            elif event.key == K_d:
                characterPosition.move_ip(3,0)
                print("d")
        elif event.type == MOUSEBUTTONDOWN:
                characterPosition.x = event.pos[0]
                characterPosition.y = event.pos[1]
        elif event.type == QUIT:
            running = 0

    mainWindow.blit(background, (0,0))
    mainWindow.blit(character, characterPosition)
    pygame.display.flip()
