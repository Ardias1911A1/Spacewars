#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class loads a spriteset and use it to create
#shots and explosions animations
#--------------------------------------------

import pygame
from pygame.locals import *

class Shots:
    def __init__(self, spriteType:str, path:str, spriteSize:tuple):
        self._spriteType = spriteType
        self._spriteset = pygame.image.load(path).convert_alpha()
        self._spriteSize = spriteSize
        self._width ,self._height = self._spriteset.get_size()
        self._spriteIndex = 0
        self._spriteTable = []

        for hCount in range(0,self._width//self._spriteSize[0]):
            self._spriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],0,self._spriteSize[0],self._spriteSize[1]))

    def animation(self):
        return self._spriteTable[self.indexLoop(self._spriteTable)]

    #Loops through a list by advancing by one index at each call.
    #If we are out of the max length of the list, it starts over at 0
    def indexLoop(self, spriteTable:list):
        if self._spriteIndex < len(spriteTable)-1:
            self._spriteIndex += 1
        else:
            self._spriteIndex = 0

        return self._spriteIndex
