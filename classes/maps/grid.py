#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class manage the grid that is shown when moving
#a unit or checking weapon range.
#--------------------------------------------
import pygame
from pygame.locals import *
from classes.tile_manager.tileset import Tileset
from classes.definitions.constants import *

class Grid:
    #constructor
    def __init__(self):
        self._GRID_TILESET = Tileset("Grid","ressources/interface/grid.png",(200,200))
        self._grids =  {"default" : self._GRID_TILESET.tileTable[0],
                        "move" : self._GRID_TILESET.tileTable[1],
                        "attack": self._GRID_TILESET.tileTable[2]}

    #accessors
    def _get_grids(self):
        return self._grids

    #mutators
    def _set_grids(self):
        self._grids = self._grids

    #destructors
    def _del_grids(self):
        del self._grids

    #help
    def _help_grids(self):
        return "Contains the 3 grid image default, moving_range, attack_range. This property must not be changed"

    #properties
    grids =     property(_get_grids, _set_grids, _del_grids, _help_grids)
