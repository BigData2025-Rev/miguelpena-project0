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
        return f"Thank you for using {self.name}. Good bye!"