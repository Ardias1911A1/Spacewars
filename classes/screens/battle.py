#--------------------------------------------
#Author: Chappuis Anthony
#Date: February 2016
#
#This class is used to display the battle animations
#--------------------------------------------

import pygame
from pygame.locals import *
from classes.units.unit import Unit
from classes.sprites.shots import Shots
import time

class Battle:
    def __init__(self):
        self._background = dict(Empty_space="ressources/backgrounds/emptySpaceBattleBackground.png",
                                Asteroids="ressources/backgrounds/asteroidsBattleBackground.png",
                                Stations="ressources/backgrounds/stationsBattleBackground.png",
                                Grass="",
                                Mountain="",
                                River="",
                                Forest="")
        self._borders = pygame.image.load("ressources/interface/battleInterface.png").convert_alpha()
        self._attackPortrait = pygame.image.load("ressources/interface/attacker.png").convert_alpha()
        self._defensePortrait = pygame.image.load("ressources/interface/defender.png").convert_alpha()
        self._shots = Shots("lasers","ressources/sprites/starships/lasers.png",(200,200))
        self._explosions = Shots("explosions","ressources/sprites/starships/explosions.png",(200,200))
        self._healthPoint = Shots("HealthPoint","ressources/interface/healthPoint.png",(5,10))

    def show(self, window:pygame.display, attackBackground:str, defenseBackground:str, unit:Unit, target:Unit, scale:tuple):
        resolution = (window.get_width(),window.get_height())
        attackBackground = pygame.image.load(self._background[attackBackground]).convert_alpha()
        attackPosition = (resolution[0]/4-scale[0]/2,resolution[1]/2-scale[1]/2)

        defenseBackground = pygame.image.load(self._background[defenseBackground]).convert_alpha()
        defensePosition = (resolution[0]*3/4-scale[0]/2,resolution[1]/2-scale[1]/2)

        unitHealthPoints = 100-int(unit.damages/unit.health*100)
        targetHealthPoints = 100-int(target.damages/target.health*100)
        shotPosition = (attackPosition[0],attackPosition[1])
        shotSpeed = 25
        firstRun = True

        for i in range(0,20):
            shotPosition = (shotPosition[0]+i*shotSpeed,shotPosition[1])
            #Graphic assets for unit (attacker)
            window.blit(attackBackground,(0,0))
            if attackPosition[0] <= shotPosition[0] <= resolution[0]/2:
                window.blit(self._shots.animation(),shotPosition)
            window.blit(unit.spriteset.movingAnimation("right"),attackPosition)

            #Graphic assets for target (defender)
            window.blit(defenseBackground,(resolution[0]/2,0))
            window.blit(target.spriteset.movingAnimation("left"),defensePosition)
            if resolution[0]/2 <= shotPosition[0] <= defensePosition[0]:
                window.blit(self._shots.animation(),shotPosition)
            elif defensePosition[0] <= shotPosition[0] <= defensePosition[0]+scale[0]:
                window.blit(self._explosions.animation(),defensePosition)

                #Damages are inflicted only once
                if firstRun:
                    targetHealthPoints = 100-int((target.damages+unit.attackForce)/target.health*100)
                    firstRun = False

            #Interface
            if (self._borders.get_width(),self._borders.get_height()) != resolution :
                borders = pygame.transform.scale(self._borders,resolution)
            else:
                borders = self._borders

            window.blit(borders,(0,0))

            #Attacker portrait and health bar
            window.blit(self._attackPortrait,(resolution[0]/10,resolution[1]/100))

            for i in range(0, unitHealthPoints):
                window.blit(self._healthPoint.animation(),(20+i*5,resolution[1]-20))

            #defender portrait and health bar
            window.blit(self._defensePortrait,(resolution[0]*9/10-scale[0],resolution[1]/100))

            for i in range(0, targetHealthPoints):
                window.blit(self._healthPoint.animation(),(resolution[0]-20-i*5,resolution[1]-20))

            pygame.display.flip()
            time.sleep(0.1)
