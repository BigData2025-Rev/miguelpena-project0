from abc import ABC, abstractmethod
from implementation.mainmenu_state import MainMenuState

class IBaseMenu(ABC):
    def run() -> None:
        ...
    def get_state() -> MainMenuState:
        ...
    