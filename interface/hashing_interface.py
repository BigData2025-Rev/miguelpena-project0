from abc import ABC, abstractmethod

class IHash(ABC):
    
    @abstractmethod
    def get_hashed_string(self) -> str:
        pass