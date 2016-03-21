#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage player informations
#--------------------------------------------

class Player:
    def __init__(self, name:str="Player", faction:str="Empire", commander:str=None, team:int=1):
        self._name = name
        self._faction = faction
        self._commander = commander
        self._team = team
        self._active = False
        self._units = []

    #accessors
    def _get_name(self):
        return self._name
    def _get_faction(self):
        return self._faction
    def _get_commander(self):
        return self._commander
    def _get_team(self):
        return self._team
    def _get_active(self):
        return self._active
    def _get_units(self):
        return self._units

    #mutators
    def _set_name(self, name:str):
        self._name = name
    def _set_faction(self, faction:str):
        self._faction = faction
    def _set_commander(self, commander:str):
        self._commander = commander
    def _set_team(self, team:int):
        self._team = team
    def _set_active(self, active:bool):
        self._active = active
    def _set_units(self, units:list):
        self._units = units

    #destructors
    def _del_name(self):
        del self._name
    def _del_faction(self):
        del self._faction
    def _del_commander(self):
        del self._commander
    def _del_team(self):
        del self._team
    def _del_active(self):
        del self._active
    def _del_units(self):
        del self._units

    #help
    def _help_name(self):
        return "Player name as string"
    def _help_faction(self):
        return "Player faction as string"
    def _help_commander(self):
        return "Player commander as string"
    def _help_team(self):
        return "Player team as integer"
    def _help_active(self):
        return "Player is active or not as boolean"
    def _help_units(self):
        return "Player units as a list of unit objects"

    #properties
    name =      property(_get_name,_set_name,_del_name,_help_name)
    faction =   property(_get_faction,_set_faction,_del_faction,_help_faction)
    commander = property(_get_commander,_set_commander,_del_commander,_help_commander)
    team =      property(_get_team,_set_team,_del_team,_help_team)
    active =    property(_get_active,_set_active,_del_active,_help_active)
    units =     property(_get_units,_set_units,_del_units,_help_units)

    #Methods
    def toggleActive(self):
        if self.active:
            self.active = False
        else:
            self.active = True
