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
from classes.screens.transition import Transition

class GameMode:
    def __init__(self, interface:Interface, players:Player=None, gameMap:GameMap=None, unitManager:UnitManager=None):
        self._interface = interface
        self._players = players
        self._gameMap = gameMap
        self._unitManager = unitManager
        self._playerTransition = Transition("ressources/interface/playerTransition.png")
        self._turn = 0

    #accessors
    def _get_interface(self):
        return self._interface

    #mutators
    def _set_interface(self, interface:Interface):
        self._interface = interface

    #destructors
    def _del_interface(self):
        del self._interface

    #help
    def _help_interface(self):
        return "Interface of the game mode as Interface object"

    #properties
    interface = property(_get_interface,_set_interface,_del_interface,_help_interface)

    #Methods
    def nextPlayer(self):
        count = 0
        for player in self._players:
            for unit in player.units:
                unit.selected = False

            if player.active:
                player.toggleActive()
                index = count + 1
                if index >= len(self._players):
                    index = 0
            count += 1
        self._players[index].toggleActive()
        return self._players[index].name

    def run(self, window:pygame.display):
        running = True
        displayTransition = False
        resolution = (window.get_width(),window.get_height())
        for player in self._players:
            self._unitManager.addUnit(player,"Cruser",self._gameMap._TILE_SIZE,(self._gameMap._mapAnchorage[0],self._gameMap._mapAnchorage[1]+self._gameMap.scale[1]*self._unitManager.count))
            self._unitManager.addUnit(player,"Cruser",self._gameMap._TILE_SIZE,(self._gameMap._mapAnchorage[0],self._gameMap._mapAnchorage[1]+self._gameMap.scale[1]*self._unitManager.count))

        #Activating first player
        self._players[0].toggleActive()
        playerName = self._players[0].name

        while(running):
            rangeType = "move"

            for menu in self._interface.menus:
                menu.mouseOverEntry(pygame.mouse.get_pos())

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
                    if event.key == K_p:
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

                    elif event.key == K_RETURN:
                        displayTransition = True
                        playerName = self.nextPlayer()

                #Mouse events
                onInterface = self._interface.isOnInterface(pygame.mouse.get_pos())
                if onInterface:
                    if event.type == MOUSEBUTTONDOWN:
                        gameMode = self._interface.actions(event)
                        if gameMode != None:
                            running = False
                else:
                    if event.type == MOUSEBUTTONDOWN:
                        self._interface.actions(event)
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
                                if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()) and player.active:
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

            #Displays transition
            if displayTransition :
                displayTransition = self._playerTransition.displayTransition(window, playerName+"'s turn")
            else:
                #Showing interface
                self._interface.show(window)
                for player in self._players:
                    if player.active:
                        self._interface.displayUnitInfos(window, player.units)


            #update Display
            pygame.display.flip()

        for player in self._players:
            self._unitManager.removeAllUnits(player)

        return gameMode
