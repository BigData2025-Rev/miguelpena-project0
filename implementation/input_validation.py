from interface.input_validation import IInputValidation
from validation_type import ValidationType

class InputValidation(IInputValidation):
    def __init__(self, input: str, validation_type: int, **kwargs: any):
        """
            When creating instance of this class, include the input and validation type enum class.
            :params: input -> string, validation_type -> enum of validation, eg. 1 -> IsANumber, 2 -> IsAMenuItem
        """
        self.input = input
        self.validation_type = validation_type
        self.validation_criteria = kwargs
    def check_if_number(self) -> bool:
        return False

    def check_if_menu_option(self) -> bool:
        return False

    def check_if_valid_string(self) -> bool:
        return False

    def is_valid(self) -> bool:
        match(self.validation_type):
            case ValidationType.IsANumber:
                return self.check_if_number()
            case ValidationType.IsAMenuOption:
                return self.check_if_menu_option()
            case ValidationType.IsValidString:
                return self.check_if_valid_string()
            case _:
                return False
