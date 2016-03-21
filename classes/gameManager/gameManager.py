#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage gamemodes, player turn, victory and defeats
#--------------------------------------------

import pygame
from pygame.locals import *
from classes.gameManager.player import Player
from classes.maps.spaceMap import SpaceMap
from classes.tile_manager.tileset import Tileset
from classes.screens.mainMenu import MainMenu

class GameManager:
    def __init__(self):
        self._gameModes = dict( mainMenu =  ["mainMenu","Main menu"],
                                campaign =  ["campaign","Start a new campaign"],
                                options =   ["options","Options"],
                                exit =      ["exit","Leave the game"])
        self._players = []
        self._turn = 0

    #accessors
    def _get_gameModes(self):
        return self._gameModes
    def _get_players(self):
        return self._players
    def _get_turn(self):
        return self._turn

    #mutators
    def _set_gameModes(self, gameModes:dict):
        self._gameModes = gameModes
    def _set_players(self, players:list):
        self._players = players
    def _set_turn(self, turn:int):
        self._turn = turn

    #destructors
    def _del_gameModes(self):
        del self._gameModes
    def _del_players(self):
        del self._players
    def _del_turn(self):
        del self._turn

    #help
    def _help_gameModes(self):
        return "Mode of the game stored as a dictionary of of list : dict(<key>=['mode id','mode caption'])"
    def _help_players(self):
        return "Players of the game stored as a list of player objects"
    def _help_turn(self):
        return "Current turn number"

    #properties
    gameModes = property(_get_gameModes,_set_gameModes,_del_gameModes,_help_gameModes)
    players =   property(_get_players,_set_players,_del_players,_help_players)
    turn =      property(_get_turn,_set_turn,_del_turn,_help_turn)

    #Methods
    def addPlayer(self, name:str="Player",faction:str="Empire",commander:str=None,team:int=1):
        self.players.append(Player(name,faction,commander,team))

    def nextTurn(self):
        self.turn += 1

    def load(self, window:pygame.display):
        running = True
        gameMode = self.gameModes["mainMenu"][0]

        while(running):
            if gameMode == self.gameModes["mainMenu"][0]:
                mainMenu = MainMenu(window,self.gameModes)
                gameMode = mainMenu.show(window)
                del mainMenu
            elif gameMode == self.gameModes["campaign"][0]:
                self.addPlayer("Ardias","Empire",None,1)
                self.addPlayer("Gorgoroth","Coalition",None,2)

                mapCode =   [["Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Empty_space","Empty_space","Stations","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Stations","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
                            ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"]]
                gameMap = SpaceMap("P4X-867",mapCode,self.players)
                gameMode = gameMap.show(window)
                del gameMap
            elif gameMode == self.gameModes["options"][0]:
                gameMode = self.gameModes["mainMenu"][0]
            elif gameMode == self.gameModes["exit"][0]:
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
