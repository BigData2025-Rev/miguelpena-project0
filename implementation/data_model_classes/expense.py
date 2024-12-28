from datetime import datetime
from dataclasses import dataclass
# from implementation.data_model_classes.expense_category import ExpenseCategory

@dataclass
class Expense():
    """
        This data class will be used to model expenses. 
    """
    expense_id: int
    account_id: int
    amount: float
    timestamp: datetime
    category: int
    # role_name: str
