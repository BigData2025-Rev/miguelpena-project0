import string
from implementation.input_validation import InputValidation
from implementation.validation_type import ValidationType
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection

from implementation.base_submenu import BaseSubmenu
from implementation.submenu_state import SubMenuState

class InitialSubMenu(BaseSubmenu):
    
    def __init__(self, name: str):
        self.current_state = SubMenuState.INITIAL
        self.submenu_options = ['Create Account', 'Login', 'Close Application']
        self.name = name
    
    def run(self):
        match(self.current_state):
            case SubMenuState.INITIAL:
                self.display()
            case _:
                print('Closing...')

    def display_submenu_options(self):
        
        print(f"\n\tWelcome to {self.name}!\n\tWhat would you lke to do?\n")
        
        for index, option in enumerate(self.submenu_options):
            print(f'\t{string.ascii_uppercase[index]}. {option}')

    def get_valid_options(self) -> str:
        return string.ascii_uppercase[:len(self.submenu_options)]


    


        
