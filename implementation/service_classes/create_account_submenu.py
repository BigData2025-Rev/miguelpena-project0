import string
from implementation.utility_classes.input_validation import InputValidation
from implementation.enum_classes.validation_type import ValidationType
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection

from implementation.service_classes.base_submenu import BaseSubmenu
from implementation.enum_classes.submenu_state import SubMenuState

class CreateAccountSubmenu(BaseSubmenu):
    def __init__(self):
        self.current_state = SubMenuState.INITIAL
        self.submenu_options = [('Username: ', ValidationType.IsValidString), ('Password: ', ValidationType.IsValidString), ('Renter Password: ', ValidationType.IsValidString), ('Monthly Income: ', ValidationType.IsANumber)]

    def display_submenu(self):
        
        print(f"\n\tCreating Account\n\tPlease enter the following:\n")
        
        for current, option in enumerate(self.submenu_options):
            print(f'\t{option[0]}', end='')
            yield current

    def get_valid(self) -> str:
        return string.ascii_uppercase[:len(self.submenu_options)]
