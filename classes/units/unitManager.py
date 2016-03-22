#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class manage units (creation, deletion and interactions)
#--------------------------------------------
import pygame
from classes.units.unit import Unit
from classes.screens.battle import Battle
from classes.gameManager.player import Player


class UnitManager:
    #constructor
    def __init__(self):
        self._count = 0
        self._units = []
        self._battle = Battle()
        self._unitRefs = { "Empire":
                                {"Cruser": dict(health=100,speed=1/10,ranges=dict(move=3,attack=1),spriteset="ressources/sprites/starships/cruser.png", attackForce=30),
                                 "Frigate": dict(health=50,speed=1/20,ranges=dict(move=4,attack=3),spriteset="ressources/sprites/starships/cruser.png", attackForce=10)},
                            "Coalition":
                                {"Cruser": dict(health=100,speed=1/4,ranges=dict(move=3,attack=1),spriteset="ressources/sprites/starships/cruser.png", attackForce=30),
                                 "Frigate": dict(health=50,speed=1/2,ranges=dict(move=4,attack=3),spriteset="ressources/sprites/starships/cruser.png", attackForce=10)},
                            "Federation":
                                {"Cruser": dict(health=100,speed=1/4,ranges=dict(move=3,attack=1),spriteset="ressources/sprites/starships/cruser.png", attackForce=30),
                                "Frigate": dict(health=50,speed=1/2,ranges=dict(move=4,attack=3),spriteset="ressources/sprites/starships/cruser.png", attackForce=10)}}

    #accessors
    def _get_units(self):
        return self._units
    def _get_count(self):
        return self._count

    #mutators
    def _set_units(self, units:list):
        self._units = units
    def _set_count(self, count:int):
        self._count = count

    #destructors
    def _del_units(self):
        del self._units
    def _del_count(self):
        del self._count

    #help
    def _help_units(self):
        return "List containing Unit class objects"
    def _help_count(self):
        return "total of units in integer"
    #properties
    units =      property(_get_units,_set_units, _del_units, _help_units)
    count =      property(_get_count,_set_count, _del_count, _help_count)

    #Methods
    def addUnit(self, player:Player, unitType:str, spriteSize:tuple, position:tuple=(0,0)):
        health = self._unitRefs[player.faction][unitType]['health']
        speed = self._unitRefs[player.faction][unitType]['speed']
        ranges = self._unitRefs[player.faction][unitType]['ranges']
        spriteset = self._unitRefs[player.faction][unitType]['spriteset']
        attackForce = self._unitRefs[player.faction][unitType]['attackForce']

        unit = Unit(player.faction, unitType, health, speed, ranges, spriteset, spriteSize, position, attackForce)

        player.units.append(unit)
        self.count += 1

    def attack(self, window:pygame.display, mapping:list, unit:Unit, target:Unit, scale:tuple):
        if unit.inRange(target.position,scale,"attack") and unit.faction != target.faction :
            attackBackground = mapping[int(unit.position[1]/scale[1])][int(unit.position[0]/scale[0])]
            defenseBackground = mapping[int(target.position[1]/scale[1])][int(target.position[0]/scale[0])]
            self._battle.show(window,attackBackground,defenseBackground, unit, target, scale)
            target.damages += unit.attackForce
            #Check if target is destroyed, if yes remove the target from map
            index = 0
            
            if target.damages >= target.health:
                self.removeUnit(index)
            index += 1

    def removeUnit(self, player:Player ,index:int):
        del player.units[index]
        self.count -= 1

    def removeAllUnits(self, player:Player):
        for unit in player.units:
            del unit
            self._count -= 1
        player.units = []
