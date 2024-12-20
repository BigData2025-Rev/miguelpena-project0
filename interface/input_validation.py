from abc import ABC, abstractmethod

class IInputValidation(ABC):
    
    @abstractmethod
    def is_valid(self) -> bool:
        ...

    