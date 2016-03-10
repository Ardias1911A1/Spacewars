#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class loads a tileset and use it to create
#different terrain's styles
#--------------------------------------------
import pygame
import random
from pygame.locals import *

class Tileset:

    #constructor
    def __init__(self, tileType:str, path:str, tileSize:tuple):
        self._tileType = tileType
        self._tileset = pygame.image.load(path).convert_alpha()
        self._width, self._height = self._tileset.get_size()
        self._tileTable = []
        self._tileSize = tileSize
        self._set_tileTable()

    #accessors
    def _get_tileTable(self):
        return self._tileTable

    def _get_tileType(self):
        return self._tileType

    def _get_tileset(self):
        return self._tileset

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height

    def _get_tileSize(self):
        return self._tileSize

    #mutators
    def _set_tileTable(self):
        self._tileTable = []
        if self._width//self._tileSize[0] > 1 or self._height//self._tileSize[1] > 1:
            for hCount in range(0,self._width//self._tileSize[0]):
                for vCount in range(0,self._height//self._tileSize[1]):
                     self._tileTable.append(self._tileset.subsurface(hCount*self._tileSize[0],vCount*self._tileSize[1],self._tileSize[0],self._tileSize[1]))
        else:
            self._tileTable.append(self._tileset)

    def _set_tileType(self, tileType:str):
        self._tileType = tileType

    def _set_tileset(self, path:str):
        self._tileset = path
        self._set_tileTable()

    def _set_width(self, width:int):
        self._width = width

    def _set_height(self, height:int):
        self._height = height

    def _set_tileSize(self, tileSize:tuple):
        self._tileSize = tileSize

    #destructors
    def _del_tileTable(self):
        del self._tileTable

    def _del_tileType(self):
        del self._tileType

    def _del_tileset(self):
        del self._tileset

    def _del_width(self):
        del self._width

    def _del_height(self):
        del self._height

    def _del_tileSize(self):
        del self._tileSize

    #help
    def _help_tileTable(self):
        return "List containing the tile table created from a tileset by the constructor"

    def _help_tileType(self):
        return "String containing the tileset type"

    def _help_tileset(self):
        return "Contains the path to source file for the tileset"

    def _help_width(self):
        return "Contains the width in pixels (integer) of the tileset linked with the class"

    def _help_height(self):
        return "Contains the height in pixels (integer) of the tileset linked with the class"

    def _help_tileSize(self):
        return "Contains the size of a tile in pixels (tuple width x height) linked with the class"

    #properties
    tileTable = property(_get_tileTable, _set_tileTable, _del_tileTable, _help_tileTable)
    tileType =  property(_get_tileType, _set_tileType, _del_tileType, _help_tileType)
    tileset =   property(_get_tileset, _set_tileset, _del_tileset, _help_tileset)
    width =     property(_get_width, _set_width, _del_width, _help_width)
    height =    property(_get_height, _set_height, _del_height, _help_height)
    tileSize =  property(_get_tileSize, _set_tileSize, _del_tileSize, _help_tileSize)

    #Methods
    #Returns on tile at random
    def getOneTileAtRandom(self):
        if len(self.tileTable)>1:
            return self.tileTable[random.randrange(0,len(self.tileTable))]
        else:
            return self.tileTable[0]
