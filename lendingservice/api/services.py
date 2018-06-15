from .models import *

class LendingService(object):
    @staticmethod
    def create_user(self, first_name, last_name, email, dob):
        self.user_data = User(
            self.first_name = first_name
            self.last_name = last_name
            self.dob = dob
            self.email = email
        )
        

    @staticmethod
    def withdraw(self):
        pass

    @staticmethod
    def make_payment(self):
        pass

    @staticmethod
    def account_status(self):
        pass

    @staticmethod
    def transactions_history(self):
        pass
