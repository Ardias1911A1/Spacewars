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
from classes.interfaces.menu import Menu
from classes.screens.mainMenu import MainMenu
from classes.interfaces.interface import Interface
from classes.gameManager.gameMode import GameMode

class GameManager:
    def __init__(self):

        #Setting players
        self._players = []
        self._players.append(Player("Ardias","Empire",None,1))
        self._players.append(Player("Gorgoroth","Coalition",None,2))
        self._players.append(Player("Khan","Federation",None,3))
        self._players.append(Player("Delgar","Federation",None,3))

        #Setting base modes
        self._gameModes = dict( options =   ["options","Options",None],
                                exit =      ["exit","Leave the game",None])

        #Constructing campagin game mode
        mapCode =   [["Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Empty_space","Empty_space","Stations","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Asteroids","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Stations","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"],
        ["Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space","Empty_space"]]

        gameMap = GameMap("P4X-86767",mapCode)

        campaignInterface = Interface(gameMap)
        campaignGameMode = GameMode(campaignInterface,self._players,gameMap,UnitManager())
        campaignMode = ["campaign","Start a new campaign",campaignGameMode]

        self._gameModes["campaign"] =  campaignMode

        #Constructing main menu game mode
        self._mainMenu = ["mainMenu","Main menu",MainMenu(self.gameModes)]

        menu1 = Menu("File","ressources/interface/menuIcon.png",[[self._mainMenu[0],self._mainMenu[1],False],[self._gameModes['exit'][0],self._gameModes['exit'][1],False]])
        menu2 = Menu("File","ressources/interface/menuIcon.png",[['test','Test',False],['test2','Test2',False]])
        menu3 = Menu("File","ressources/interface/menuIcon.png",[['test','Test',False],['test2','Test2',False]])
        menus = [menu1,menu2,menu3]

        self.gameModes["campaign"][2].interface.menus = menus

    #accessors
    def _get_gameModes(self):
        return self._gameModes
    def _get_players(self):
        return self._players
    def _get_mainMenu(self):
        return self._mainMenu

    #mutators
    def _set_gameModes(self, gameModes:dict):
        self._gameModes = gameModes
    def _set_players(self, players:list):
        self._players = players
    def _set_mainMenu(self, mainMenu:list):
        self._mainMenu = mainMenu

    #destructors
    def _del_gameModes(self):
        del self._gameModes
    def _del_players(self):
        del self._players
    def _del_mainMenu(self):
        del self._mainMenu

    #help
    def _help_gameModes(self):
        return "Mode of the game stored as a dictionary of of list : dict(<key>=['mode id','mode caption',game mode object])"
    def _help_players(self):
        return "Players of the game stored as a list of player objects"
    def _help_mainMenu(self):
        return "Main menu of the game as a list : ['mode id','mode caption',main menu object]"

    #properties
    gameModes = property(_get_gameModes,_set_gameModes,_del_gameModes,_help_gameModes)
    players =   property(_get_players,_set_players,_del_players,_help_players)
    mainMenu =  property(_get_mainMenu,_set_mainMenu,_del_mainMenu,_help_mainMenu)

    #Methods
    def addPlayer(self, name:str="Player",faction:str="Empire",commander:str=None,team:int=1):
        self.players.append(Player(name,faction,commander,team))

    def load(self, window:pygame.display):
        running = True
        gameMode = self.mainMenu[0]

        while(running):
            if gameMode == self.gameModes["campaign"][0]:
                gameMode = self.gameModes["campaign"][2].run(window)
            elif gameMode == self.gameModes["options"][0]:
                gameMode = None
            elif gameMode == self.gameModes["exit"][0]:
                running = False
            else:
                gameMode = self.mainMenu[2].show(window)

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
