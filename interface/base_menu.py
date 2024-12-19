from abc import ABC, abstractmethod

class IBaseMenu(ABC):
    @abstractmethod
    def run(self) -> None:
        """
            This method handles the menu logic until the state becomes menu_state.CLOSING_STATE
            
            This method will raise the menuselectioninvalid exception if the user does not provide a valid input. 
            :params: 
            :return: 
        """
        pass

    @abstractmethod
    def set_state(state: int) -> None:
        """
            Encapsulation method for setting the current state of the menu object.

            :params: The MainMenuState class holds the various valid program states.  
            :return:
        """
        pass

    @abstractmethod
    def get_state() -> int:
        """
            Encapsulation method for getting the current state of the menu object.

            :params:
            :return: This will be an int associated with the MainMenuState class.
        """
        pass

    @abstractmethod
    def display_menu(self) -> None:
        """
            Method for displaying menu options and listening for user input.
            :params:
            :return:
        """
        pass
