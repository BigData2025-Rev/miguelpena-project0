from implementation.data_model_classes.account import Account
from interface.accountdataaccess_interface import IAccountDataAccess
from implementation.utility_classes.data_handler import DataHandler

class AccountDAO(IAccountDataAccess):
    def __init__(self):
        self.data_handler = DataHandler()

    def get_account_by_username(self, username: str) -> Account:
        pass
    
    def create_account(self, account: Account) -> Account:
        pass

    # def update_account(self, account: Account) -> bool:
    #     pass

    # def delete_account_by_username(self, username: str) -> bool:
    #     pass


