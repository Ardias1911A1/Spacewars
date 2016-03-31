#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage a menu
#--------------------------------------------

import pygame

from classes.definitions.constants import *

class Menu:
    def __init__(self,name:str,icon:str=None,entries:list=None,position:tuple=(0,0)):
        self._name = name
        self._position = position
        self._icon = pygame.image.load(icon).convert_alpha()
        self._entries = entries
        self._active = False
        self._font = DEFAULT_FONT
        self._fontSize = 12

    #accessors
    def _get_name(self):
        return self._name
    def _get_position(self):
        return self._position
    def _get_icon(self):
        return self._icon
    def _get_entries(self):
        return self._entries
    def _get_active(self):
        return self._active

    #mutators
    def _set_name(self, name:str):
        self._name = name
    def _set_position(self, position:tuple):
        self._position = position
    def _set_icon(self, iconPath:str):
        self._icon = pygame.image.load(iconPath).convert_alpha()
    def _set_entries(self, entries:list):
        self._entries = entries
    def _set_active(self, active:bool):
        self._active = active

    #destructors
    def _del_name(self):
        del self._name
    def _del_position(self):
        del self._position
    def _del_icon(self):
        del self._icon
    def _del_entries(self):
        del self._entries
    def _del_active(self):
        del self._active

    #help
    def _help_name(self):
        return "Menu's name as string"
    def _help_position(self):
        return "Menu's position as a tuple (x,y)"
    def _help_icon(self):
        return "Menu's icon as pygame Surface, the constructor receive the image filepath as string and loads the image in the attribute"
    def _help_entries(self):
        return "Contains menu entries as a 2d list : ['text to be shown','action']"
    def _help_active(self):
        return "Indicates if menu is active as boolean"

    #properties
    name =      property(_get_name,_set_name,_del_name,_help_name)
    position =  property(_get_position,_set_position,_del_position,_help_position)
    icon =      property(_get_icon,_set_icon,_del_icon,_help_icon)
    entries =   property(_get_entries,_set_entries,_del_entries,_help_entries)
    active =    property(_get_active,_set_active,_del_active,_help_active)

    #Methods
    def show(self,window:pygame.display):
        entryCount = 0
        for entry in self.entries:
            text = pygame.font.Font(self._font,self._fontSize).render(entry[0],16,(0,255,0))
            window.blit(text,(self.position[0],self.icon.get_height()+entryCount*self._fontSize+2))
            entryCount += 1
