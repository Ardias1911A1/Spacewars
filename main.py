import pygame
from pygame.locals import *
from classes.tile_manager.tileset import Tileset
import random
from classes.screens.mainMenu import MainMenu
from classes.gameManager.gameManager import GameManager
from classes.maps.spaceMap import SpaceMap
from classes.definitions.constants import *

def main():
    #Initialisation
    pygame.init()
    infoObject = pygame.display.Info()
    mainWindow = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
    pygame.display.set_caption(GAME_TITLE)
    appIcon = pygame.image.load("spacewars.png").convert_alpha()
    pygame.display.set_icon(appIcon)
    pygame.key.set_repeat(10, 10)
    mainMenu = MainMenu(mainWindow)
    gameManager = GameManager()
    nextAction = gameManager.gameModes[0]
    running = True

    while(running):
        if nextAction == "menu":
            nextAction = mainMenu.show(mainWindow)
        elif nextAction == "start":
            mapCode =   [["Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Empty_space","Empty_space","Stations","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Stations","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"]]
            gameMap = SpaceMap("P4X-867",mapCode)
            nextAction = gameMap.show(mainWindow)
            del gameMap
        elif nextAction == "options":
            nextAction = "menu"
        elif nextAction == "exit":
            running = False

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

if __name__ == '__main__': main()
