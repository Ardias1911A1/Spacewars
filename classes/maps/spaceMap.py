#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class manage the construction of game maps and terrain
#according parameters and fonctions
#--------------------------------------------
import pygame
from pygame.locals import *
from classes.tile_manager.tileset import Tileset
from classes.units.unitManager import UnitManager
from classes.units.unit import Unit
from classes.maps.grid import Grid
from classes.maps.tile import Tile
from classes.gameManager.player import Player
from classes.interfaces.interface import Interface
import time

class SpaceMap:
    #constructor
    def __init__(self, name:str, mapping:str):
        self._name = name
        self._mapping = mapping
        self._width = len(mapping[0])
        self._height = len(mapping)
        self._TILE_SIZE = (200,200)
        self._scaling = 1.0
        self._scale = (int(self._TILE_SIZE[0]*self._scaling),int(self._TILE_SIZE[1]*self._scaling))

        self._EMPTY_SPACE_TILESET = Tileset("Empty_space","ressources/tilesets/space/emptySpace.png",self._TILE_SIZE)
        self._ASTEROIDS_TILESET = Tileset("Asteroids","ressources/tilesets/space/asteroids.png",self._TILE_SIZE)
        self._STATIONS_TILESET = Tileset("Stations","ressources/tilesets/space/stations.png",self._TILE_SIZE)
        self._grid = Grid()

        self._unitManager = UnitManager()
        self._interface = Interface(self._unitManager.units)
        self._mapAnchorage = (0,0)

        self._players = []

        self._players.append(Player("Player 1","Empire","Ardias",1))
        self._players.append(Player("Player 2","Coalition","Godrig",2))

        self._map = []
        #Fills a map with tiles taken randomly from the tileset according to the dimensions of the map.
        for hCount in range(0,self._width):
            array = []
            for vCount in range(0,self._height):
                if self._mapping[vCount][hCount] == self._ASTEROIDS_TILESET.tileType:
                    tile = Tile(self._ASTEROIDS_TILESET.tileType,self._ASTEROIDS_TILESET.getOneTileAtRandom())
                elif self._mapping[vCount][hCount] == self._STATIONS_TILESET.tileType:
                    tile = Tile(self._STATIONS_TILESET.tileType,self._STATIONS_TILESET.getOneTileAtRandom())
                else:
                    tile = Tile(self._EMPTY_SPACE_TILESET.tileType,self._EMPTY_SPACE_TILESET.getOneTileAtRandom())
                array.append(tile)
            self._map.append(array)

    #accessors
    def _get_name(self):
        return self._name
    def _get_mapping(self):
        return self._mapping
    def _get_width(self):
        return self._width
    def _get_height(self):
        return self._height
    def _get_scale(self):
        return self._scale
    def _get_scaling(self):
        return self._scaling
    def _get_grid(self):
        return self._grid

    #mutators
    def _set_name(self, name:str):
        self._name = name
    def _set_mapping(self, mapping:str):
        self._mapping = mapping
    def _set_width(self, width:int):
        self._width = width
    def _set_height(self, height:int):
        self._height = height
    def _set_scale(self, scale:tuple):
        self._scale = scale

    def _set_scaling(self, scaling:float):
        if scaling <= 0.4:
            scaling = 0.4
        elif scaling >= 2:
            scaling = 2
        self._scaling = scaling
        self._set_scale((int(self._TILE_SIZE[0]*scaling), int(self._TILE_SIZE[1]*scaling)))

    def _set_grid(self, grid:Grid):
        self._grid = grid

    #destructors
    def _del_name(self):
        del self._name
    def _del_mapping(self):
        del self._mapping
    def _del_width(self):
        del self._width
    def _del_height(self):
        del self._height
    def _del_scale(self):
        del self._scale
    def _del_scaling(self):
        del self._scaling
    def _del_grid(self):
        del self._grid

    #help
    def _help_name(self):
        return "Contains map name as string"
    def _help_mapping(self):
        return "Contains the reference file used to construct the map as string"
    def _help_width(self):
        return "Contains the width of the map (number of horizontal tiles) as int"
    def _help_height(self):
        return "Contains the height of the map (number of vertical tiles) as int"
    def _help_scale(self):
        return "Contains a tuple constructed from TILE_SIZE and scaling. It gives the final size of each tile to be shown\
                at screen after scaling. Mainly used as part of the zoom features on the game maps"
    def _help_scaling(self):
        return "Contains the factor used to transform TILE_SIZE to scale which is used to defin images final on screen size"
    def _help_grid(self):
        return "Contains a Grid object responsible for showing the grid range when moving or shooting with a unit"

    #properties
    name =      property(_get_name, _set_name, _del_name, _help_name)
    mapping =   property(_get_mapping, _set_mapping, _del_mapping, _help_mapping)
    width =     property(_get_width, _set_width, _del_width, _help_width)
    height =    property(_get_height, _set_height, _del_height, _help_height)
    scale =     property(_get_scale, _set_scale, _del_scale, _help_scale)
    scaling =   property(_get_scaling, _set_scaling, _del_scaling, _help_scaling)
    grid =      property(_get_grid, _set_grid, _del_grid, _help_grid)

    #Methods
    #This method draws the background of the map by displaying each element of self._map at the
    #correct coordinates and with the chosen scaling
    def drawMap(self, window:pygame.display, units:list=None, rangeType:str="move", scale:tuple=None, position:tuple=None):
        hCount = 0

        if position == None:
            position = self._mapAnchorage

        if scale == None:
            scale = self.scale

        for array in self._map:
            vCount = 0
            for tile in array:
                tileImage = tile.image
                gridTile = self.grid.grids['default']
                coordinates = (hCount*scale[0]+position[0],vCount*scale[1]+position[1])
                #Scales assets only if not displayed with their original resolution
                if scale != self._TILE_SIZE:
                    tileImage = pygame.transform.scale(tileImage,scale)
                    gridTile = pygame.transform.scale(gridTile,scale)
                window.blit(tileImage,coordinates)
                #Check if a unit is selected and if so, activate the tactical grids
                if units != None:
                    for unit in units:
                        if unit.selected:
                            #Check if the tile is within unit move range.
                            if unit.inRange(coordinates,scale,rangeType):
                                gridTile = self.grid.grids[rangeType]

                            #Scales assets only if not displayed with their original resolution
                            if scale != self._TILE_SIZE:
                                gridTile = pygame.transform.scale(gridTile,scale)
                            window.blit(gridTile,coordinates)
                vCount += 1
            hCount += 1

    def zoom(self, inOrOut:str):
        #We have to store the difference of tile size before the scaling
        #in order to correct the sprite's position after the scaling
        factor = []
        for unit in self._unitManager.units:
            factor.append((unit.position[0]/self.scale[0],unit.position[1]/self.scale[1]))

        mapFactor = (self._mapAnchorage[0]/self.scale[0],self._mapAnchorage[1]/self.scale[1])

        if inOrOut == "in":
            self.scaling += 0.2
        else:
            self.scaling -= 0.2

        count = 0
        for unit in self._unitManager.units:
            unit.position = (factor[count][0]*self.scale[0],factor[count][1]*self.scale[1])
            unit.destination = unit.position
            count +=1

        self._mapAnchorage = (mapFactor[0]*self.scale[0],mapFactor[1]*self.scale[1])

    #Check if a tile is occupied by another unit
    def isDestinationEmpty(self, destination:tuple):
        for unit in self._unitManager.units :
            if destination == unit.position:
                return False, unit

        return True, None
    #Used to correct given coordinates to a multiple of the scale attribute
    def normalizeCoordinatesToGrid(self, coordinates:tuple):
        coordinates = (coordinates[0]-self._mapAnchorage[0],coordinates[1]-self._mapAnchorage[1])
        xAxis = self.scale[0]*int(coordinates[0]/self.scale[0])+self._mapAnchorage[0]
        yAxis = self.scale[1]*int(coordinates[1]/self.scale[1])+self._mapAnchorage[1]
        return (xAxis,yAxis)

    #Used to move map around to display off screen parts
    def moveMap(self, direction:str, units:list = None):
        if direction == "up":
            move = (0,self.scale[1]/10)
        elif direction == "down":
            move = (0,-self.scale[1]/10)
        elif direction == "left":
            move = (self.scale[0]/10,0)
        elif direction == "right":
            move = (-self.scale[0]/10,0)
        else:
            move = (0,0)

        self._mapAnchorage = (self._mapAnchorage[0]+move[0], self._mapAnchorage[1]+move[1])

        if units != None:
            for unit in units:
                position = (unit.position[0]+move[0],unit.position[1]+move[1])
                position = (unit.position[0]+move[0],unit.position[1]+move[1])
                unit.position = position
                unit.destination = unit.position

    def show(self,  window: pygame.display):

        self._unitManager.addUnit("Empire","Cruser",self._TILE_SIZE)
        self._unitManager.addUnit("Empire","Cruser",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))
        self._unitManager.addUnit("Federation","Cruser",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))
        self._unitManager.addUnit("Federation","Cruser",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))
        self._unitManager.addUnit("Coalition","Cruser",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))
        self._unitManager.addUnit("Coalition","Cruser",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))

        resolution = (window.get_width(),window.get_height())
        spriteSelected = False
        move = False
        clock = pygame.time.Clock()

        #Activating first player
        self._players[0].toggleActive()

        while(True):
            rangeType = "move"
            clock.tick(30)
            background = pygame.Surface(resolution)
            window.blit(background,(0,0))

            #CHecks if mouse on screen side and if we must move the map
            mousePosition = pygame.mouse.get_pos()
            if mousePosition[1] <= 5:
                self.moveMap("up", self._unitManager.units)
            if mousePosition[1] >= resolution[1]-5:
                self.moveMap("down", self._unitManager.units)
            if mousePosition[0] <= 5:
                self.moveMap("left", self._unitManager.units)
            if mousePosition[0] >= resolution[0]-5:
                self.moveMap("right", self._unitManager.units)

            #Events
            for event in pygame.event.get():
                #Keyboard events
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return "menu"
                    elif event.key == K_KP_PLUS:
                        self._unitManager.addUnit("Empire","Frigate",self._TILE_SIZE,(0,self.scale[1]*self._unitManager.count))
                    elif event.key == K_KP_MINUS:
                        index = 0
                        for unit in self._unitManager.units:
                            if unit.selected:
                                self._unitManager.removeUnit(index)
                            index += 1
                    elif event.key == K_r:
                        rangeType = "attack"

                    elif event.key == K_UP:
                        self.moveMap("up", self._unitManager.units)
                    elif event.key == K_DOWN:
                        self.moveMap("down", self._unitManager.units)
                    elif event.key == K_LEFT:
                        self.moveMap("left", self._unitManager.units)
                    elif event.key == K_RIGHT:
                        self.moveMap("right", self._unitManager.units)

                #Mouse events
                if event.type == MOUSEBUTTONDOWN:
                    #Wheel up
                    if event.button == 4:
                        self.zoom("in")
                    #Wheel down
                    if event.button == 5:
                        self.zoom("out")

                    for unit in self._unitManager.units:
                        rect = unit.getUnitRect(self.scale)
                        #Selecting a unit
                        if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                            unit.selected = True
                        #Deselecting a unit
                        elif pygame.mouse.get_pressed()[0] and not (rect.collidepoint(pygame.mouse.get_pos())):
                            unit.selected = False
                        #Right clic on destination for selected unit
                        if pygame.mouse.get_pressed()[2] and unit.selected:
                            destination = self.normalizeCoordinatesToGrid(pygame.mouse.get_pos())
                            target = self.isDestinationEmpty(destination)
                            if target[0]:
                                unit.destination = destination
                            else:
                                self._unitManager.attack(window,self._mapping,unit,target[1],self.scale)

                #Misc events
                if event.type == QUIT:
                    exit()

            #Constructing the background with scaling option
            self.drawMap(window, self._unitManager.units, rangeType)

            #units display
            for unit in self._unitManager.units:
                #Moving selected unit to destination
                if unit.position != unit.destination :
                    unit.move(self.scale)
                else:
                    unit.idle()

                #Scales assets only if not displayed with their original resolution
                if self.scale != self._TILE_SIZE:
                    sprite = pygame.transform.scale(unit.sprite,self.scale)
                else:
                    sprite = unit.sprite

                window.blit(sprite,unit.position)

            #Showing interface
            self._interface.show(window)
            #show minimap
            miniMapPosition = (int(resolution[0]*7/8),int(resolution[1]*5/6))

            #Making sure the minimap will not go out of screen
            maxVertSize = self._interface.bottomInterface.get_height()-10
            maxHorSize = (self._interface.bottomInterface.get_width()/12)

            mapVertTileCount = len(self.mapping)
            mapHorTileCount = len(self.mapping[0])
            miniMapTileSize = (int(maxHorSize/mapHorTileCount),int(maxVertSize/mapVertTileCount))

            #Choose the maximum size of the tiles by checking if width is bigger than height or opposite
            if miniMapTileSize[0] > miniMapTileSize[1]:
                miniMapTileSize = (miniMapTileSize[1],miniMapTileSize[1])
            else:
                miniMapTileSize = (miniMapTileSize[0],miniMapTileSize[0])

            miniMapTileSizeOn2 = (int(miniMapTileSize[0]/2),int(miniMapTileSize[1]/2))

            sizeFactor = ((mapHorTileCount*miniMapTileSize[0])/(mapHorTileCount*self.scale[0]) , (mapVertTileCount*miniMapTileSize[1])/(mapVertTileCount*self.scale[1]))

            self.drawMap(window, None,rangeType,miniMapTileSize,miniMapPosition)

            #unit display on minimap
            for unit in self._unitManager.units:
                position = (int((unit.position[0]-self._mapAnchorage[0])*sizeFactor[0]+miniMapPosition[0]+miniMapTileSizeOn2[0]),int((unit.position[1]-self._mapAnchorage[1])*sizeFactor[1]+miniMapPosition[1]+miniMapTileSizeOn2[1]))
                if unit.faction == "Empire":
                    pygame.draw.circle(window, (200,0,0), position, 3, 0)
                elif unit.faction == "Coalition":
                    pygame.draw.circle(window, (0,100,150), position, 3, 0)
                elif unit.faction == "Federation":
                    pygame.draw.circle(window, (0,200,100), position, 3, 0)

            #screen update
            pygame.display.flip()
