#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage gamemodes, player turn, victory and defeats
#--------------------------------------------

import pygame
from pygame.locals import *
from classes.gameManager.player import Player
from classes.maps.gameMap import GameMap
from classes.units.unitManager import UnitManager
from classes.screens.mainMenu import MainMenu
from classes.interfaces.interface import Interface
from classes.gameManager.gameMode import GameMode

class GameManager:
    def __init__(self):

        mapCode =   [["Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Empty_space","Empty_space","Stations","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Stations","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                    ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"]]

        self._players = []
        self._players.append(Player("Ardias","Empire",None,1))
        self._players.append(Player("Gorgoroth","Coalition",None,2))

        self._gameModes = dict( mainMenu =  ["mainMenu","Main menu",None],
                                campaign =  ["campaign","Start a new campaign",GameMode(Interface(),self._players,GameMap("P4X-86767",mapCode),UnitManager())],
                                options =   ["options","Options",None],
                                exit =      ["exit","Leave the game",None])
    #accessors
    def _get_gameModes(self):
        return self._gameModes
    def _get_players(self):
        return self._players

    #mutators
    def _set_gameModes(self, gameModes:dict):
        self._gameModes = gameModes
    def _set_players(self, players:list):
        self._players = players

    #destructors
    def _del_gameModes(self):
        del self._gameModes
    def _del_players(self):
        del self._players

    #help
    def _help_gameModes(self):
        return "Mode of the game stored as a dictionary of of list : dict(<key>=['mode id','mode caption'])"
    def _help_players(self):
        return "Players of the game stored as a list of player objects"

    #properties
    gameModes = property(_get_gameModes,_set_gameModes,_del_gameModes,_help_gameModes)
    players =   property(_get_players,_set_players,_del_players,_help_players)

    #Methods
    def addPlayer(self, name:str="Player",faction:str="Empire",commander:str=None,team:int=1):
        self.players.append(Player(name,faction,commander,team))

    def load(self, window:pygame.display):
        running = True
        gameMode = self.gameModes["mainMenu"][0]

        while(running):
            if gameMode == self.gameModes["mainMenu"][0]:
                mainMenu = MainMenu(window,self.gameModes)
                gameMode = mainMenu.show(window)
                del mainMenu
            elif gameMode == self.gameModes["campaign"][0]:
                gameMode = self.gameModes["campaign"][2].run(window)
            elif gameMode == self.gameModes["options"][0]:
                gameMode = self.gameModes["mainMenu"][0]
            elif gameMode == self.gameModes["exit"][0]:
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
