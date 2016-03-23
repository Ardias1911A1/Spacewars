#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class displays a transition animation
#--------------------------------------------

import pygame

from classes.definitions.constants import *

class Transition:
    def __init__(self, imagePath:str, text:str):
        self._image = pygame.image.load(imagePath).convert_alpha()
        self._text = text
        self._font = DEFAULT_FONT
        self._animation = []
        self._index = 0
        for hCount in range(0,self._image.get_width()//1920):
            self._animation.append(self._image.subsurface(hCount*1920,0,1920,1080))

    def displayTransition(self, window:pygame.display):
        resolution = (window.get_width(),window.get_height())
        image = self._animation[self._index]
        imageRes = (image.get_width(),image.get_height())

        #scaling assets if image resolution is not window resolution
        if resolution != imageRes:
            image = pygame.transform.scale(image,resolution)

        title = pygame.font.Font(self._font,22).render(self._text,16,(0,200,0))
        titleWidthOn2 = title.get_width()/2
        titleHeightOn2 = title.get_height()/2

        window.blit(image,(0,0))
        window.blit(title,(resolution[0]/2-titleWidthOn2,resolution[1]/2-titleHeightOn2))

        if self._index >= len(self._animation)-1:
            self._index = 0
            return False
        else:
            self._index += 1
            return True
