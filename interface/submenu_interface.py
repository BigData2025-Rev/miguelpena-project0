from abc import ABC, abstractmethod

class ISubMenu(ABC):
    @abstractmethod
    def run(self) -> None:
        pass
    
    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def display_submenu_options(self) -> None:
        pass
    
    @abstractmethod
    def get_valid_options(self) -> str:
        pass