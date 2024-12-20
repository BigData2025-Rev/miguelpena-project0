import pytest
from implementation.input_validation import InputValidation
from implementation.validation_type import ValidationType

input_validation: InputValidation | None = None

def test_validate_number_input():
    input_validation = InputValidation('g', ValidationType.IsANumber)
    result = input_validation.is_valid()
    assert result == False