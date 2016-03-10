#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class define units
#--------------------------------------------

import pygame
from pygame.locals import *
from classes.sprites.spriteset import Spriteset

class Unit:
    #constructor
    def __init__(self, faction:str="", unitType:str="", health:int=0, speed:int=0, ranges:dict={"move":1,"attack":1}, spriteset:Spriteset="", spriteSize:tuple=(0,0), position:tuple=(0,0), attackForce:int=10):
        self._faction = faction
        self._unitType = unitType
        self._name = unitType
        self._health = health
        self._damages = 0
        self._speed = speed
        self._ranges = ranges
        self._spriteset = Spriteset(unitType, spriteset, spriteSize)
        self._position = position
        self._destination = position
        self._sprite = self.spriteset.idleSprite()
        self._selected = False
        self._attackForce = attackForce

    #accessors
    def _get_name(self):
        return self._name
    def _get_faction(self):
        return self._faction
    def _get_unitType(self):
        return self._unitType
    def _get_health(self):
        return self._health
    def _get_damages(self):
        return self._damages
    def _get_speed(self):
        return self._speed
    def _get_ranges(self):
        return self._ranges
    def _get_spriteset(self):
        return self._spriteset
    def _get_sprite(self):
        return self._sprite
    def _get_position(self):
        return self._position
    def _get_destination(self):
        return self._destination
    def _get_selected(self):
        return self._selected
    def _get_attackForce(self):
        return self._attackForce

    #mutators
    def _set_name(self, name:str):
        self._name = name
    def _set_faction(self, faction:str):
        self._faction = faction
    def _set_unitType(self, unitType:str):
        self._unitType = unitType
    def _set_health(self, health:int):
        self._health = health
    def _set_damages(self, damages:int):
        self._damages = damages
    def _set_speed(self, speed:int):
        self._speed = speed
    def _set_ranges(self, ranges:dict):
        self._ranges = ranges
    def _set_spriteset(self, spriteset:str):
        self._spriteset = spriteset
    def _set_sprite(self, sprite:pygame.Surface):
        self._sprite = sprite
    def _set_position(self, position:tuple):
        self._position = position
    def _set_destination(self, destination:tuple):
        self._destination = destination
    def _set_selected(self, selected:bool):
        self._selected = selected
    def _set_attackForce(self, attackForce:int):
        self._attackForce = attackForce
    #destructors
    def _del_name(self):
        del self._name
    def _del_faction(self):
        del self._faction
    def _del_unitType(self):
        del self._unitType
    def _del_health(self):
        del self._health
    def _del_damages(self):
        del self._damages
    def _del_speed(self):
        del self._speed
    def _del_ranges(self):
        del self._ranges
    def _del_spriteset(self):
        del self._spriteset
    def _del_sprite(self):
        del self._sprite
    def _del_position(self):
        del self._position
    def _del_destination(self):
        del self._destination
    def _del_selected(self):
        del self._selected
    def _del_attackForce(self):
        del self._attackForce
    #help
    def _help_name(self):
        return "Name of the unit. Stored as string"
    def _help_faction(self):
        return "Faction of the unit. Stored as string"
    def _help_unitType(self):
        return "Type of the unit. Stored as string"
    def _help_health(self):
        return "Maximum health of the unit. Stored as integer"
    def _help_damages(self):
        return "Damages taken by the unit. Stored as integer"
    def _help_speed(self):
        return "Speed of the unit in pixels per cycle stored as integer."
    def _help_ranges(self):
        return "Move and attack range of the unit in number of tiles stored as integer in a dictionary \{ 'move':int, 'attack':int\}."
    def _help_spriteset(self):
        return "Spriteset of the unit stored as spriteset object, see Spriteset class for more details"
    def _help_sprite(self):
        return "Sprite of the unit on the map. Stored as pygame Surface"
    def _help_position(self):
        return "Position of the unit on the map. Stored as tuple"
    def _help_destination(self):
        return "Destination of the unit on the map. Stored as tuple"
    def _help_selected(self):
        return "Defines if the unit is selected or not. Stored as boolean"
    def _help_attackForce(self):
        return "Attack force of the unit as integer"

    #properties
    name =          property(_get_name,_set_name, _del_name, _help_name)
    faction =       property(_get_faction,_set_faction, _del_faction, _help_faction)
    unitType =      property(_get_unitType,_set_unitType, _del_unitType, _help_unitType)
    health =        property(_get_health,_set_health, _del_health, _help_health)
    damages =       property(_get_damages,_set_damages, _del_damages, _help_damages)
    speed =         property(_get_speed,_set_speed, _del_speed, _help_speed)
    ranges =        property(_get_ranges,_set_ranges, _del_ranges, _help_ranges)
    spriteset =     property(_get_spriteset,_set_spriteset, _del_spriteset, _help_spriteset)
    sprite =        property(_get_sprite,_set_sprite, _del_sprite, _help_sprite)
    position =      property(_get_position,_set_position, _del_position, _help_position)
    destination =   property(_get_destination,_set_destination, _del_destination, _help_destination)
    selected =      property(_get_selected,_set_selected, _del_selected, _help_selected)
    attackForce =   property(_get_attackForce,_set_attackForce, _del_attackForce, _help_attackForce)

    #Methods
    def getUnitRect(self,scale:tuple):
        return self.sprite.get_rect(topleft=self.position,width=scale[0], height=scale[1])
    # Take the current unit position and the event and move the unit
        # from tileset object
    def move(self, scale:tuple):
        if self.inRange(self.destination,scale,"move"):
            self.selected = False
            movement = (scale[0]*self.speed,scale[1]*self.speed)
            if self.position[1] > self.destination[1]:
                self.sprite = self.spriteset.movingAnimation("up")
                self.position = self.position[0],self.position[1]-movement[1]

            elif self.position[1] < self.destination[1]:
                self.sprite = self.spriteset.movingAnimation("down")
                self.position = self.position[0],self.position[1]+movement[1]

            elif self.position[0] > self.destination[0]:
                self.sprite = self.spriteset.movingAnimation("left")
                self.position = self.position[0]-movement[0],self.position[1]

            elif self.position[0] < self.destination[0]:
                self.sprite = self.spriteset.movingAnimation("right")
                self.position = self.position[0]+movement[0],self.position[1]
            else:
                self.idle()

    def idle(self):
        self.sprite = self.spriteset.idleSprite()

    def inRange(self, coordinates:tuple, scale:tuple, rangeType:str="move"):
        #Check if the tile is within unit range. The range is shown as number of tile the unit can move each turn.
        if  ((coordinates[0] <= self.position[0] + scale[0]*self.ranges[rangeType] - (coordinates[1] - self.position[1]) and
            coordinates[1] <= self.position[1] + scale[1]*self.ranges[rangeType] - (coordinates[0] - self.position[0])) and

            (coordinates[0] >= self.position[0] - scale[0]*self.ranges[rangeType] - (coordinates[1] - self.position[1]) and
            coordinates[1] >= self.position[1] - scale[1]*self.ranges[rangeType] - (coordinates[0] - self.position[0])) and

            (coordinates[0] <= self.position[0] + scale[0]*self.ranges[rangeType] + (coordinates[1] - self.position[1]) and
            coordinates[1] <= self.position[1] + scale[1]*self.ranges[rangeType] + (coordinates[0] - self.position[0])) and

            (coordinates[0] >= self.position[0] - scale[0]*self.ranges[rangeType] + (coordinates[1] - self.position[1]) and
            coordinates[1] >= self.position[1] - scale[1]*self.ranges[rangeType] + (coordinates[0] - self.position[0]))):

            return True
        else:
            return False
