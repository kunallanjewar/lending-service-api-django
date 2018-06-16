from .models import *

class LendingService(object):
    @staticmethod
    def create_user(data):
        user_data = User(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
        )
        return (user_data)

    @staticmethod
    def open_account(self, credit_line, principal_balance):
        pass

    @staticmethod
    def account_status(self):
        pass

    @staticmethod
    def withdraw(self):
        pass

    @staticmethod
    def make_payment(self):
        pass

    @staticmethod
    def transactions_history(self):
        pass
