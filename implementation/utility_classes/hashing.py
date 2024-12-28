import bcrypt
from interface.hashing_interface import IHash

class Hashing(IHash):
    def __init__(self, input_string: str):
        """
            When creating an object of this class, provide the string that will be hashed.
        """
        self.hashed_value = bcrypt.hashpw(input_string.encode(), bcrypt.gensalt())

    def get_hashed_string(self) -> str:
        return self.hashed_value.decode()
    
    @staticmethod
    def check_match(input_string: str, hashed_string: str) -> bool:
        return bcrypt.checkpw(input_string.encode(), hashed_string.encode())