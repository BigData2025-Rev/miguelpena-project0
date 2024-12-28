from implementation.service_classes.initial_submenu import InitialSubMenu
from implementation.enum_classes.submenu_state import SubMenuState
from implementation.enum_classes.mainmenu_state import MainMenuState
from interface.menu_interface import IMenu

class MainMenu(IMenu):
    def __init__(self, name):
        self.current_state = MainMenuState.INITIAL
        self.current_submenu = None
        self.name = name

    def run(self) -> None:
        match(self.current_state):
            case MainMenuState.INITIAL:
                self.current_submenu = InitialSubMenu(self.name)
                self.current_submenu.run()
                self.current_state = MainMenuState.SUBSTATE
            case MainMenuState.SUBSTATE:
                self.wait_for_submenu()
            case _:
                print(self.get_parting_message())

    def set_state(self, state: int) -> None:
        self.current_state = state

    def get_state(self) -> int:
        return self.current_state
    
    def reset_state(self) -> None:
        self.current_state = MainMenuState.INITIAL

    def reset_data(self) -> None:
        self.current_submenu = None

    def wait_for_submenu(self) -> None:
        self.current_submenu.run()
        if self.current_submenu.get_state() == SubMenuState.CLOSING:
            self.reset_state()
            self.reset_data()

    def get_parting_message(self) -> str:
        """
            This method is explicitly used before quitting the program. 
            :params:
            :return: This method returns a string with a parting message.
        """
        return f"Thank you for using {self.name}. Good bye!"