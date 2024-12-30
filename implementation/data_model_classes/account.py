from dataclasses import dataclass
from implementation.utility_classes.hashing import Hashing

@dataclass
class Account():
    """
        This data class will be used to model accounts gathered by joining the accounts and roles table. 

        Normalization is upto 2F, since there are transient dependencies on this table.

        Information can be displayed to doctors and admins. 
    """
    account_id: int
    account_username: str
    account_password: str
    first_name: str
    last_name: str
    monthly_income: float
    # role_name: str
    def check_matching_password(self, entered_password) -> bool:
        hashed_object = Hashing()
        hashed_object.set_hashed_string(self.account_password)
        return hashed_object.is_a_match(entered_password)
    
    def hash_password(self, new_password: str):
        hashed_object = Hashing(new_password)
        self.account_password = hashed_object.get_hashed_string()
