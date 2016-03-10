#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class loads a spriteset and use it to create
#units' animations and appearance
#--------------------------------------------

import pygame
from pygame.locals import *
import random

class Spriteset:
    #constructor
    def __init__(self, spriteType:str, path:str, spriteSize:tuple):
        self._spriteType = spriteType
        self._spriteset = pygame.image.load(path).convert_alpha()
        self._width ,self._height = self._spriteset.get_size()
        self.spriteSize = spriteSize
        self._spriteIndex = 0

        self._lastDirection = "right"

        self._upSpriteTable = []
        self._downSpriteTable = []
        self._leftSpriteTable = []
        self._rightSpriteTable = []
        self._idleUpSpriteTable = []
        self._idleDownSpriteTable = []
        self._idleLeftSpriteTable = []
        self._idleRightSpriteTable = []
        self._set_spriteTable()

    #accessors
    def _get_lastDirection(self):
        return self._lastDirection

    def _get_upSpriteTable(self):
        return self._upSpriteTable
    def _get_downSpriteTable(self):
        return self._downSpriteTable
    def _get_leftSpriteTable(self):
        return self._leftSpriteTable
    def _get_rightSpriteTable(self):
        return self._rightSpriteTable

    def _get_idleUpSpriteTable(self):
        return self._idleUpSpriteTable
    def _get_idleDownSpriteTable(self):
        return self._idleDownSpriteTable
    def _get_idleLeftSpriteTable(self):
        return self._idleLeftSpriteTable
    def _get_idleRightSpriteTable(self):
        return self._idleRightSpriteTable

    def _get_spriteType(self):
        return self._spriteType

    def _get_spriteset(self):
        return self._spriteset

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height

    def _get_spriteSize(self):
        return self._spriteSize

    #mutators
    def _set_lastDirection(self, lastDirection:str):
        self._lastDirection = lastDirection

    def _set_spriteTable(self):
        self._upSpriteTable = []
        self._downSpriteTable = []
        self._leftSpriteTable = []
        self._rightSpriteTable = []
        self._idleUpSpriteTable = []
        self._idleDownSpriteTable = []
        self._idleLeftSpriteTable = []
        self._idleRightSpriteTable = []
        for hCount in range(0,self._width//self._spriteSize[0]):
            self._upSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],0*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._downSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],1*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._leftSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],2*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._rightSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],3*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._idleUpSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],4*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._idleDownSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],5*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._idleLeftSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],6*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))
            self._idleRightSpriteTable.append(self._spriteset.subsurface(hCount*self._spriteSize[0],7*self._spriteSize[1],self._spriteSize[0],self._spriteSize[1]))

    def _set_spriteType(self, spriteType:str):
        self._spriteType = spriteType

    def _set_spriteset(self, path:str):
        self._spriteset = path
        self._set_spriteTable()

    def _set_width(self, width:int):
        self._width = width

    def _set_height(self, height:int):
        self._height = height

    def _set_spriteSize(self, spriteSize:tuple):
        self._spriteSize = spriteSize

    #destructors
    def _del_lastDirection(self):
        del self._lastDirection

    def _del_upSpriteTable(self):
        del self._upSpriteTable

    def _del_downSpriteTable(self):
        del self._downSpriteTable

    def _del_leftSpriteTable(self):
        del self._leftSpriteTable

    def _del_rightSpriteTable(self):
        del self._rightSpriteTable

    def _del_idleUpSpriteTable(self):
        del self._idleUpSpriteTable
    def _del_idleDownSpriteTable(self):
        del self._idleDownSpriteTable
    def _del_idleLeftSpriteTable(self):
        del self._idleLeftSpriteTable
    def _del_idleRightSpriteTable(self):
        del self._idleRightSpriteTable

    def _del_spriteType(self):
        del self._spriteType

    def _del_spriteset(self):
        del self._spriteset

    def _del_width(self):
        del self._width

    def _del_height(self):
        del self._height

    def _del_spriteSize(self):
        del self._spriteSize

    #help
    def _help_lastDirection(self):
        return "Return last know direction of the sprite (up, down, left or right)"

    def _help_upSpriteTable(self):
        return "return a table containing the sprites for the unit going up"
    def _help_downSpriteTable(self):
        return "return a table containing the sprites for the unit going down"
    def _help_leftSpriteTable(self):
        return "return a table containing the sprites for the unit going left"
    def _help_rightSpriteTable(self):
        return "return a table containing the sprites for the unit going right"

    def _help_idleUpSpriteTable(self):
        return "return a table containing the up oriented sprites for non-moving unit "
    def _help_idleDownSpriteTable(self):
        return "return a table containing the down oriented sprites for non-moving unit "
    def _help_idleLeftSpriteTable(self):
        return "return a table containing the left oriented sprites for non-moving unit "
    def _help_idleRightSpriteTable(self):
        return "return a table containing right oriented the sprites for non-moving unit "

    def _help_spriteType(self):
        return "String containing the spriteset type"

    def _help_spriteset(self):
        return "Contains the path to source file for the spriteset"

    def _help_width(self):
        return "Contains the width in pixels (integer) of the spriteset linked with the class"

    def _help_height(self):
        return "Contains the height in pixels (integer) of the spriteset linked with the class"

    def _help_spriteSize(self):
        return "Contains the size of a sprite in pixels (tuple width x height) linked with the class"

    #properties
    lastDirection =         property(_get_lastDirection, _set_lastDirection, _del_lastDirection, _help_lastDirection)

    upSpriteTable =         property(_get_upSpriteTable, _set_spriteTable, _del_upSpriteTable, _help_upSpriteTable)
    downSpriteTable =       property(_get_downSpriteTable, _set_spriteTable, _del_downSpriteTable, _help_downSpriteTable)
    leftSpriteTable =       property(_get_leftSpriteTable, _set_spriteTable, _del_leftSpriteTable, _help_leftSpriteTable)
    rightSpriteTable =      property(_get_rightSpriteTable, _set_spriteTable, _del_rightSpriteTable, _help_rightSpriteTable)

    idleUpSpriteTable =     property(_get_idleUpSpriteTable, _set_spriteTable, _del_idleUpSpriteTable, _help_idleUpSpriteTable)
    idleDownSpriteTable =   property(_get_idleDownSpriteTable, _set_spriteTable, _del_idleDownSpriteTable, _help_idleDownSpriteTable)
    idleLeftSpriteTable =   property(_get_idleLeftSpriteTable, _set_spriteTable, _del_idleLeftSpriteTable, _help_idleLeftSpriteTable)
    idleRightSpriteTable =  property(_get_idleRightSpriteTable, _set_spriteTable, _del_idleRightSpriteTable, _help_idleRightSpriteTable)

    spriteType =            property(_get_spriteType, _set_spriteType, _del_spriteType, _help_spriteType)
    spriteset =             property(_get_spriteset, _set_spriteset, _del_spriteset, _help_spriteset)
    width =                 property(_get_width, _set_width, _del_width, _help_width)
    height =                property(_get_height, _set_height, _del_height, _help_height)
    spriteSize =            property(_get_spriteSize, _set_spriteSize, _del_spriteSize, _help_spriteSize)

    #Methods
    #Return the idle graphics for the sprite corresponding to
    #his last moving direction
    def idleSprite(self):
        if self.lastDirection == "up":
            return self.idleUpSpriteTable[self.indexLoop(self.idleUpSpriteTable)]
        elif self.lastDirection == "down":
            return self.idleDownSpriteTable[self.indexLoop(self.idleDownSpriteTable)]
        elif self.lastDirection == "left":
            return self.idleLeftSpriteTable[self.indexLoop(self.idleLeftSpriteTable)]
        elif self.lastDirection == "right":
            return self.idleRightSpriteTable[self.indexLoop(self.idleRightSpriteTable)]

    #Returns the sprite's graphic for the moving animation.
    def movingAnimation(self, direction:str):
        self.lastDirection = direction

        if direction == "up":
            sprite = self.upSpriteTable[self.indexLoop(self.upSpriteTable)]

        elif direction == "down":
            sprite = self.downSpriteTable[self.indexLoop(self.downSpriteTable)]

        elif direction == "left":
            sprite = self.leftSpriteTable[self.indexLoop(self.leftSpriteTable)]

        elif direction == "right":
            sprite = self.rightSpriteTable[self.indexLoop(self.rightSpriteTable)]

        return sprite

    #Loops through a list by advancing by one index at each call.
    #If we are out of the max length of the list, it starts over at 0
    def indexLoop(self, spriteTable:list):
        if self._spriteIndex < len(spriteTable)-1:
            self._spriteIndex += 1
        else:
            self._spriteIndex = 0

        return self._spriteIndex
