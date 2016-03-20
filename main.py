import pygame
from pygame.locals import *
from classes.gameManager.gameManager import GameManager
from classes.definitions.constants import *

def main():
    #Initialisation
    pygame.init()
    infoObject = pygame.display.Info()
    window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
    pygame.display.set_caption(GAME_TITLE)
    appIcon = pygame.image.load("spacewars.png").convert_alpha()
    pygame.display.set_icon(appIcon)
    pygame.key.set_repeat(10, 10)
    gameManager = GameManager()
    gameManager.load(window)

if __name__ == '__main__': main()
