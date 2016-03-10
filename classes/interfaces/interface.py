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
        self._miniMap = None

    def show(self, window:pygame.display):
        windowResolution = (window.get_width(),window.get_height())

        windowHeightOn10 = int(windowResolution[1]/10)
        windowHeightOn5 = int(windowResolution[1]/5)

        topResolution = (windowResolution[0],windowHeightOn10)
        bottomResolution = (windowResolution[0],windowHeightOn5)

        #scaling images if they are different from the current resolution
        if (self._topInterface.get_width(), self._topInterface.get_height()) != topResolution :
            topInterface = pygame.transform.scale(self._topInterface,topResolution)
        else:
            topInterface = self._topInterface

        if (self._bottomInterface.get_width(),self._bottomInterface.get_height()) != bottomResolution:
            bottomInterface = pygame.transform.scale(self._bottomInterface,bottomResolution)
        else:
            bottomInterface = self._bottomInterface

        window.blit(topInterface,ANCHOR_AT_00)
        window.blit(bottomInterface,(0,windowResolution[1]-windowHeightOn5))
