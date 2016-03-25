#--------------------------------------------
#Author: Chappuis Anthony
#Date: March 2016
#
#This class is used to manage a menu
#--------------------------------------------


class Menu:
    def __init__(self,name:str, icon:str=None, entries:list=None):
        self._name = name
        self._icon = icon
        self._entries = entries

    #accessors
    def _get_name(self):
        return self._name
    def _get_icon(self):
        return self._icon
    def _get_entries(self):
        return self._entries

    #mutators
    def _set_name(self, name:str):
        self._name = name
    def _set_icon(self, iconPath:str):
        self._icon = iconPath
    def _set_entries(self, entries:list):
        self._entries = entries

    #destructors
    def _del_name(self):
        del self._name
    def _del_icon(self):
        del self._icon
    def _del_entries(self):
        del self._entries
    #help
    def _help_name(self):
        return "Menu's name as string"
    def _help_icon(self):
        return "Menu's icon filePath as string"
    def _help_entries(self):
        return "Contains menu entries as a 2d list : ['text to be shown','action']"
    #properties
    name =      property(_get_name,_set_name,_del_name,_help_name)
    icon =      property(_get_icon,_set_icon,_del_icon,_help_icon)
    entries =   property(_get_entries,_set_entries,_del_entries,_help_entries)
