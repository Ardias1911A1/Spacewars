#--------------------------------------------
#Author: Chappuis Anthony
#Date: Mars 2016
#
#This class is used to display the tactical maps interface
#--------------------------------------------
import pygame
from pygame.locals import *

from classes.definitions.constants import *

class Interface:
    def __init__(self):
        self._topInterface = pygame.image.load("ressources/interface/topInterface.png").convert_alpha()
        self._bottomInterface = pygame.image.load("ressources/interface/bottomInterface.png").convert_alpha()

    #accessors
    def _get_topInterface(self):
        return self._topInterface

    def _get_bottomInterface(self):
        return self._bottomInterface
    #mutators
    def _set_topInterface(self, path:str):
        self._topInterface = pygame.image.load(path).convert_alpha()

    def _set_bottomInterface(self, path:str):
        self._bottomInterface = pygame.image.load(path).convert_alpha()
    #destructors
    def _del_topInterface(self):
        del self._topInterface

    def _del_bottomInterface(self):
        del self._bottomInterface
    #help
    def _help_topInterface(self):
        return "Contains the image for the top interface"

    def _help_bottomInterface(self):
        return "Contains the image for the bottom interface"
    #properties

    topInterface =      property(_get_topInterface,_set_topInterface,_del_topInterface,_help_topInterface)
    bottomInterface =   property(_get_bottomInterface,_set_bottomInterface,_del_bottomInterface,_help_bottomInterface)

    def show(self, window:pygame.display):
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
