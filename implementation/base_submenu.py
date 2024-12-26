from custom_exceptions.invalid_menu_selection import InvalidMenuSelection
from interface.submenu_interface import ISubMenu
from implementation.input_validation import InputValidation
from implementation.validation_type import ValidationType

class BaseSubmenu(ISubMenu):
    def display(self):
        
        input_valid = False
        validation = None

        while not input_valid:
            self.display_submenu_options()
            user_input = input('>>>')
            valid_options = self.get_valid_options()
            validation = InputValidation(user_input, ValidationType.IsAMenuOption, valid_options=valid_options)
            try:
                if validation.is_valid():
                    input_valid = True
            except InvalidMenuSelection as e:
                print(e.message)