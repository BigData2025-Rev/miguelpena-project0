from mainmenu_state import MainMenuState
from interface.base_menu import IBaseMenu

class MainMenu(IBaseMenu):
    def __init__(self, name):
        self.name = name

    def run() -> None:
        pass

    def get_state() -> MainMenuState:
        pass

    def get_parting_message(self) -> str:
        """
            This method is explicitly used before quitting the program. 
            :params:
            :return: This method returns a string with a parting message.
        """
        return f"Thank you for using {self.name}. Good bye!"