#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage a Tile (a tile is a case in the games)
#--------------------------------------------

import pygame

class Tile:
    def __init__(self,tileType:str=None, image:pygame.surface=None):
        self._position = (0,0)
        self._tileType = tileType
        self._image = image

    #mutators
    def _get_position(self):
        return self._position
    def _get_tileType(self):
        return self._tileType
    def _get_image(self):
        return self._image

    #accessors
    def _set_position(self, position:tuple):
        self._position = position
    def _set_tileType(self, tileType:str):
        self._tileType = tileType
    def _set_image(self, image:pygame.surface):
        self._image = image

    #destructors
    def _del_position(self):
        del self._position
    def _del_tileType(self):
        del self._tileType
    def _del_image(self):
        del self._image

    #help
    def _help_position(self):
        return "Stores tile position as a tuple"
    def _help_tileType(self):
        return "Stores tile type as str"
    def _help_image(self):
        return "Stores tile image as pygame surface"

    #properties

    position = property(_get_position,_set_position,_help_position,_del_position)
    tileType = property(_get_tileType,_set_tileType,_help_tileType,_del_tileType)
    image =    property(_get_image,_set_image,_help_image,_del_image)
