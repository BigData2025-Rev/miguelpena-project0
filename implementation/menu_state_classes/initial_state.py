from interface.base_menu_state import BaseMenuState
from implementation.menu_state_classes.initial_submenu import InitialSubMenu
from implementation.main_menu import MainMenu

class InitialState(BaseMenuState):
    def __init__(self, menu: MainMenu):
        self.menu = menu
        self.submenu = InitialSubMenu(self, menu.get_name())

    def execute(self):
        self.submenu.display()
    
    def close(self):
        self.menu.current_state = self.menu.initial_state