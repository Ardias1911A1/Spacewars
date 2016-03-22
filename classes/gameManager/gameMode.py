#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class loads and manage game modes
#--------------------------------------------

import pygame
from pygame.locals import *

from classes.interfaces.interface import Interface
from classes.maps.gameMap import GameMap
from classes.units.unitManager import UnitManager
from classes.gameManager.player import Player

class GameMode:
    def __init__(self, interface:Interface, players:Player=None, gameMap:GameMap=None, unitManager:UnitManager=None):
        self._interface = interface
        self._players = players
        self._gameMap = gameMap
        self._unitManager = unitManager
        self._turn = 0

    #Methods
    def run(self, window:pygame.display):
        running = True
        resolution = (window.get_width(),window.get_height())
        for player in self._players:
            self._unitManager.addUnit(player,"Cruser",self._gameMap._TILE_SIZE,(self._gameMap._mapAnchorage[0],self._gameMap._mapAnchorage[1]+self._gameMap.scale[1]*self._unitManager.count))
            self._unitManager.addUnit(player,"Cruser",self._gameMap._TILE_SIZE,(self._gameMap._mapAnchorage[0],self._gameMap._mapAnchorage[1]+self._gameMap.scale[1]*self._unitManager.count))

        #Activating first player
        self._players[0].toggleActive()

        while(running):
            rangeType = "move"

            #Checks if mouse on screen side and if we must move the map
            mousePosition = pygame.mouse.get_pos()
            if mousePosition[1] <= 5:
                self._gameMap.moveMap("up")
            if mousePosition[1] >= resolution[1]-5:
                self._gameMap.moveMap("down")
            if mousePosition[0] <= 5:
                self._gameMap.moveMap("left")
            if mousePosition[0] >= resolution[0]-5:
                self._gameMap.moveMap("right")

            #Events
            for event in pygame.event.get():
                #Keyboard events
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_p:
                        for player in self._players:
                            if player.active:
                                self._unitManager.addUnit(player,"Frigate",self._TILE_SIZE,(self._gameMap._mapAnchorage[0],self._gameMap._mapAnchorage[1]+self._gameMap.scale[1]*self._unitManager.count))
                    elif event.key == K_m:
                        for player in self._players:
                            index = 0
                            for unit in player.units:
                                if unit.selected:
                                    self._unitManager.removeUnit(player,index)
                                index += 1
                    elif event.key == K_r:
                        rangeType = "attack"

                    elif event.key == K_UP:
                        self._gameMap.moveMap("up")
                    elif event.key == K_DOWN:
                        self._gameMap.moveMap("down")
                    elif event.key == K_LEFT:
                        self._gameMap.moveMap("left")
                    elif event.key == K_RIGHT:
                        self._gameMap.moveMap("right")

                #Mouse events
                if event.type == MOUSEBUTTONDOWN:
                    #Wheel up
                    if event.button == 4:
                        self._gameMap.zoom("in")
                    #Wheel down
                    if event.button == 5:
                        self._gameMap.zoom("out")

                    for player in self._players:
                        for unit in player.units:
                            rect = unit.getUnitRect(self._gameMap.scale)
                            #Selecting a unit
                            if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                                unit.selected = True
                            #Deselecting a unit
                            elif pygame.mouse.get_pressed()[0] and not (rect.collidepoint(pygame.mouse.get_pos())):
                                unit.selected = False
                            #Right clic on destination for selected unit
                            if pygame.mouse.get_pressed()[2] and unit.selected:
                                destination = self._gameMap.normalizeCoordinatesToGrid(pygame.mouse.get_pos())
                                target = self._gameMap.isDestinationEmpty(destination)
                                if target[0]:
                                    unit.destination = destination
                                else:
                                    self._unitManager.attack(window,self._gameMap._mapping,unit,target[1],self._gameMap.scale,self._players)

                #Misc events
                if event.type == QUIT:
                    exit()

            self._gameMap.show(window, rangeType, self._players)

        for player in self._players:
            self._unitManager.removeAllUnits(player)

        return "mainMenu"
