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
        self._topInterface = "ressources/interface/topInterface.png"
        self._topInterfaceImage = pygame.image.load(self._topInterface).convert_alpha()
        self._topInterfacePosition = (0,0)
        self._bottomInterface = "ressources/interface/bottomInterface.png"
        self._bottomInterfaceImage = pygame.image.load(self._bottomInterface).convert_alpha()
        self._bottomInterfacePosition = (0,0)
        self._miniMap = miniMap
        self._font = DEFAULT_FONT
        self._fontSize = 12
        self._menus = menus

        menuCount = 0
        for menu in self._menus:
            menu.position = (menuCount*64,0)
            menuCount += 1

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
        self._topInterface = path
        self._topInterfaceImage = pygame.image.load(path).convert_alpha()
    def _set_bottomInterface(self, path:str):
        self._bottomInterface = path
        self._bottomInterfaceImage = pygame.image.load(path).convert_alpha()
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
        return "Contains the image path for the top interface as string"
    def _help_bottomInterface(self):
        return "Contains the image path for the bottom interface as string"
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

    def isOnInterface(self, position:tuple):
        interfacePositions = []
        interfacePositions.append(self._topInterfaceImage.get_rect(topleft=self._topInterfacePosition,width=self._topInterfaceImage.get_width(), height=self._topInterfaceImage.get_height()))
        interfacePositions.append(self._bottomInterfaceImage.get_rect(topleft=self._bottomInterfacePosition,width=self._bottomInterfaceImage.get_width(), height=self._bottomInterfaceImage.get_height()))

        collision = False
        for rect in interfacePositions:
            if rect.collidepoint(position):
                collision = True

        return collision

    #Recieve events from the player via gamemode and execute interface's actions (example: menu clic)
    def actions(self,event):
        #If clic is on a menu
        for menu in self._menus:
            rect = menu.icon.get_rect(topleft=menu.position,width=menu.icon.get_width(), height=menu.icon.get_height())
            if rect.collidepoint(event.pos):
                menu.active = True
            else:
                menu.active = False


    def show(self, window:pygame.display):
        #Backgrounds of the interface
        windowResolution = (window.get_width(),window.get_height())

        windowHeightOn10 = int(windowResolution[1]/10)
        windowHeightOn5 = int(windowResolution[1]/5)

        topResolution = (windowResolution[0],windowHeightOn10)
        bottomResolution = (windowResolution[0],windowHeightOn5)

        #scaling images if they are different from the current resolution
        if (self._topInterfaceImage.get_width(), self._topInterfaceImage.get_height()) != topResolution :
            self._topInterfaceImage = pygame.transform.scale(self._topInterfaceImage,topResolution)

        if (self._bottomInterfaceImage.get_width(),self._bottomInterfaceImage.get_height()) != bottomResolution:
            self._bottomInterfaceImage = pygame.transform.scale(self._bottomInterfaceImage,bottomResolution)

        self._bottomInterfacePosition = (0,windowResolution[1]-self._bottomInterfaceImage.get_height())

        #Shows Backgrounds
        window.blit(self._topInterfaceImage,self._topInterfacePosition)
        window.blit(self._bottomInterfaceImage,self._bottomInterfacePosition)

        #Shows menus
        for menu in self.menus:
            menuPosition = menu.position
            icon = menu.icon
            window.blit(icon, menuPosition)
            #Showing menu entries
            if menu.active:
                menu.show(window)

        #show minimap
        miniMapPosition = (int(windowResolution[0]*6/7),int(windowResolution[1]*5/6))
        self.miniMap.drawMap(window,"move",miniMapPosition,True, self._bottomInterfaceImage.get_height()-10,self._bottomInterfaceImage.get_width()//15-10)
