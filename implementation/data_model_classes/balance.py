from datetime import datetime
from dataclasses import dataclass

@dataclass
class Balance():
    """
        This data class will be used to model balance for keeping track of the current monthly income minus expenses. 
    """
    balance_id: int
    account_id: int
    amount: float
    timestamp: datetime
    # role_name: str
