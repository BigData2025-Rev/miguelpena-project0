from dataclasses import dataclass

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
