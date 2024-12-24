import re
from interface.input_validation import IInputValidation
from implementation.validation_type import ValidationType
from custom_exceptions.invalid_number_input import InvalidNumberInput

class InputValidation(IInputValidation):
    def __init__(self, input: str, validation_type: int, **kwargs: any):
        """
            When creating instance of this class, include the input and validation type enum class.
            :params: input -> string, validation_type -> enum of validation, eg. 1 -> IsANumber, 2 -> IsAMenuItem
        """
        self.input = input
        self.validation_type = validation_type
        self.validation_criteria = kwargs
    
    def check_if_float(self) -> float:
        try: 
            result = float(self.input)
            return result
        except ValueError as ve:
            raise InvalidNumberInput("Please enter a number.")
    
    def check_if_number(self) -> tuple:
        # """
        #     This method uses regular expression to ensure that user input is a number.
        #     As a refresher here are a few rules: 
        #     \\d -> matches 0-9 
        #     + -> one or more 
        #     ? -> zero or one
        #     ^ -> starts with following re expression
        #     $ -> ends with prior re expression
        #     \\ -> followed by a character indicates a specific character, 
        #     for example \\- specifies that I'm looking for the negative sign, or \\. indicates 
        #     a period and not the re symbol for matching any character.
        # """
        numeric_format = re.compile(r'^\-?\d+\.?\d+$')
        match_obj = re.search(numeric_format, self.input)
        if match_obj == None:
            raise InvalidNumberInput("Please enter a number.")
    
        if int(self.input) < 0:
            raise InvalidNumberInput("Please enter a positive number.")
        

        return (True, int(self.input))

    def check_if_menu_option(self) -> tuple:
        return False

    def check_if_valid_string(self) -> tuple:
        return False

    def is_valid(self) -> tuple:
        match(self.validation_type):
            case ValidationType.IsANumber:
                return self.check_if_number()
            case ValidationType.IsAMenuOption:
                return self.check_if_menu_option()
            case ValidationType.IsValidString:
                return self.check_if_valid_string()
            case _:
                return False
