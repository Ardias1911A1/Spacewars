#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage gamemodes, player turn, victory and defeats
#--------------------------------------------

from classes.gameManager.player import Player

class GameManager:
    def __init__(self, players:list=None):
        self._gameModes = ["menu","campaign","skirmish","options","exit"]
        self._players = players
        self._turn = None

    #accessors
    def _get_gameModes(self):
        return self._gameModes
    def _get_players(self):
        return self._players
    def _get_turn(self):
        return self._turn

    #mutators
    def _set_gameModes(self, gameModes:list):
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
        return "Mode of the game stored as a list of string"
    def _help_players(self):
        return "Players of the game stored as a list of player objects"
    def _help_turn(self):
        return "Current turn number"

    #properties
    gameModes = property(_get_gameModes,_set_gameModes,_del_gameModes,_help_gameModes)
    players = property(_get_players,_set_players,_del_players,_help_players)
    turn = property(_get_turn,_set_turn,_del_turn,_help_turn)

    #Methods
    def add_player(self, name:str="Player",faction:str="Empire",commander:str=None,team:int=1):
        self.player.append(Player(name,faction,commander,team))
