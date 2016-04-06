#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class represents the main menu every other part
#of the game are called from here.
#--------------------------------------------
import pygame
from pygame.locals import *
from classes.sprites.spriteset import Spriteset
from classes.tile_manager.tileset import Tileset
from classes.definitions.constants import *
import time

class MainMenu:
    #constructor
    def __init__(self, gameModes:dict, font:str=DEFAULT_FONT, fontColor:tuple=(200,0,0)):
        self._background = pygame.image.load("ressources/main_title_background.png").convert()
        self._starship = Spriteset("Cruser","ressources/sprites/starships/cruser.png",(200,200))
        self._planet = Tileset("Planet","ressources/tilesets/space/planet1.png",(800,800))
        self._font = font
        self._title = GAME_TITLE
        self._titleFontSize = 64
        self._titleFontColor = fontColor

        self._entries = []
        for key, gameMode in gameModes.items():
            self._entries.append([False,gameMode[1],gameMode[0]])

        self._fontSize = 24
        self._fontColor = fontColor
    #Methods
    def show(self, window: pygame.display):
        resolution = (window.get_width(), window.get_height())
        while(True):
            #Defining various screen coordinats from game's resolution in order
            #to dynamically place the menu's elements and preparing is assets
            screenXCenter = resolution[0]//2
            screenYCenter = resolution[1]//2
            screenYQuarter = resolution[1]//4
            self._starship.lastDirection = "right"
            starship = self._starship.idleSprite()
            title = pygame.font.Font(self._font,self._titleFontSize).render(self._title,16,self._titleFontColor)
            planet = self._planet.getOneTileAtRandom()
            titleWidthOn2 = title.get_rect().width//2
            starshipWidthOn2 = starship.get_rect().width//2
            titlePosition = (screenXCenter-titleWidthOn2, screenYQuarter)
            starshipPosition = (screenXCenter-starshipWidthOn2,screenYQuarter*3)

            #The menu is dynamically constructed
            window.blit(self._background,ANCHOR_AT_00)
            window.blit(planet,ANCHOR_AT_00)
            window.blit(title, titlePosition)
            entrySpacing = resolution[1]//10
            totalEntriesOn2 = len(self._entries)//3
            entryYPosition = screenYCenter - (entrySpacing*totalEntriesOn2)
            pointerPosition = pygame.mouse.get_pos()
            count = 0

            for entry in self._entries:
                menuEntry = pygame.font.Font(self._font,self._fontSize).render(entry[1],16,self._fontColor)
                entryWidthOn2 = menuEntry.get_width()//2
                entryPosition = (screenXCenter-entryWidthOn2, entryYPosition+entrySpacing*count)
                entryRect = menuEntry.get_rect(center=(entryPosition[0],entryPosition[1]),width=menuEntry.get_width()*2,height=menuEntry.get_height()*2)

                #Check if mouse is over the current menu's entry
                if entryRect.collidepoint(pointerPosition):
                    for e in self._entries:
                        e[0] = False
                    entry[0] = True

                if entry[0]:
                    menuEntry = pygame.font.Font(self._font,self._fontSize).render(entry[1],16,(0,255,0))

                window.blit(menuEntry,entryPosition)
                count += 1

            window.blit(starship,starshipPosition)
            pygame.display.flip()

            time.sleep(0.1)

            for event in pygame.event.get():
                #Return to main function the next action to do
                if event.type == MOUSEBUTTONDOWN:
                    for entry in self._entries:
                        if entry[0]:
                            return entry[2]
                #Moving through the menu
                if event.type == KEYDOWN:
                    if event.key == (K_UP or K_w):
                        entryCount = 0
                        for entry in self._entries:
                            if entry[0]:
                                entry[0] = False
                                pos = entryCount-1
                                if pos < 0:
                                    pos = 0
                            entryCount += 1
                        self._entries[pos][0] = True
                    if event.key == (K_DOWN or K_s):
                        entryCount = 0
                        for entry in self._entries:
                            if entry[0]:
                                entry[0] = False
                                pos = entryCount+1
                                maxPos = len(self._entries)-1
                                if pos > maxPos:
                                    pos = maxPos
                            entryCount += 1
                        self._entries[pos][0] = True
                    if event.key == K_RETURN:
                        for entry in self._entries:
                            if entry[0]:
                                return entry[2]
                #Leaves application
                if event.type == QUIT:
                    exit()
