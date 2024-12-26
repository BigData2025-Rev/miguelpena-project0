from mainmenu_state import MainMenuState
from interface.base_menu import IBaseMenu

class MainMenu(IBaseMenu):
    def __init__(self, name):
        self.current_state = MainMenuState.INITIAL
        self.current_submenu = None
        self.name = name

    def run() -> None:
        pass

    def set_state(self, state: int) -> None:
        self.current_state = state

    def get_state(self) -> int:
        return self.current_state
    
    def reset_state(self) -> None:
        self.current_state = MainMenuState.INITIAL

    def reset_date(self) -> None:
        self.submenu_dict.clear()

    def display_menu(self) -> None:
        pass

    def get_parting_message(self) -> str:
        """
            This method is explicitly used before quitting the program. 
            :params:
            :return: This method returns a string with a parting message.
        """
        return f"Thank you for using {self.name}. Good bye!"