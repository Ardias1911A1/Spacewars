#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to display the tactical maps interface
#--------------------------------------------
import pygame
from pygame.locals import *

from classes.definitions.constants import *
from classes.maps.gameMap import GameMap

class Interface:
    def __init__(self, miniMap:GameMap=None, menus:list=None):
        self._topInterface = pygame.image.load("ressources/interface/topInterface.png").convert_alpha()
        self._bottomInterface = pygame.image.load("ressources/interface/bottomInterface.png").convert_alpha()
        self._miniMap = miniMap
        self._font = DEFAULT_FONT
        self._fontSize = 12
        self._menus = menus

    #accessors
    def _get_topInterface(self):
        return self._topInterface
    def _get_bottomInterface(self):
        return self._bottomInterface
    def _get_miniMap(self):
        return self._miniMap
    def _get_menus(self):
        return self._menus

    #mutators
    def _set_topInterface(self, path:str):
        self._topInterface = pygame.image.load(path).convert_alpha()
    def _set_bottomInterface(self, path:str):
        self._bottomInterface = pygame.image.load(path).convert_alpha()
    def _set_miniMap(self, miniMap:GameMap):
        self._miniMap = miniMap
    def _set_menus(self, menus:list):
        self._menus = menus

    #destructors
    def _del_topInterface(self):
        del self._topInterface
    def _del_bottomInterface(self):
        del self._bottomInterface
    def _del_miniMap(self):
        del self._miniMap
    def _del_menus(self):
        del self._menus

    #help
    def _help_topInterface(self):
        return "Contains the image for the top interface"
    def _help_bottomInterface(self):
        return "Contains the image for the bottom interface"
    def _help_miniMap(self):
        return "Contains mini Map as map object"
    def _help_menus(self):
        return "Contains interface's menus as a list of menu objects"

    #properties
    topInterface =      property(_get_topInterface,_set_topInterface,_del_topInterface,_help_topInterface)
    bottomInterface =   property(_get_bottomInterface,_set_bottomInterface,_del_bottomInterface,_help_bottomInterface)
    miniMap =           property(_get_miniMap,_set_miniMap,_del_miniMap,_help_miniMap)
    menus =             property(_get_menus,_set_menus,_del_menus,_help_menus)

    def displayUnitInfos(self,window:pygame.display, units:list):
        windowResolution = (window.get_width(),window.get_height())
        position = (10,int(windowResolution[1]*5/6))

        for unit in units:
            if unit.selected:
                currentHealth = unit.health - unit.damages
                maxHealth = unit.health

                infos = ("Health : "+str(currentHealth)+" / "+str(maxHealth),"Move range : "+str(unit.ranges["move"]))
                count = 0
                for text in infos:
                    coordinates = (position[0],position[1]+self._fontSize*count)
                    entry = pygame.font.Font(self._font,self._fontSize).render(text,16,(0,255,0))
                    window.blit(entry,coordinates)
                    count += 1

    def show(self, window:pygame.display):
        #Backgrounds of the interface
        windowResolution = (window.get_width(),window.get_height())

        windowHeightOn10 = int(windowResolution[1]/10)
        windowHeightOn5 = int(windowResolution[1]/5)

        topResolution = (windowResolution[0],windowHeightOn10)
        bottomResolution = (windowResolution[0],windowHeightOn5)

        #scaling images if they are different from the current resolution
        if (self.topInterface.get_width(), self.topInterface.get_height()) != topResolution :
            topInterface = pygame.transform.scale(self.topInterface,topResolution)
        else:
            topInterface = self.topInterface

        if (self.bottomInterface.get_width(),self.bottomInterface.get_height()) != bottomResolution:
            bottomInterface = pygame.transform.scale(self.bottomInterface,bottomResolution)
        else:
            bottomInterface = self.bottomInterface

        window.blit(topInterface,ANCHOR_AT_00)
        window.blit(bottomInterface,(0,windowResolution[1]-windowHeightOn5))

        #show minimap
        miniMapPosition = (int(windowResolution[0]*6/7),int(windowResolution[1]*5/6))
        self.miniMap.drawMap(window,"move",miniMapPosition,True, self._bottomInterface.get_height()-10,self.bottomInterface.get_width()//15-10)
