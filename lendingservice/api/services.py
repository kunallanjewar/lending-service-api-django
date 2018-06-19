
class LendingService(object):

    def __init__(self,
                credit_line=0,
                apr=0.35,
                interest=0.0,
                principal_balance=0.0,
                days=0):

        self._credit_line = credit_line
        self.apr = apr
        self._interest = interest
        self.principal_balance = principal_balance
        self.days = days

    @property
    def apr_fixed(self):
        return self.apr

    @property
    def credit_line(self):
        import random
        CREDIT_LINE = (500, 1500, 2500, 5000)
        return random.choice(CREDIT_LINE)

    @property
    def random_credit_line(self):
        import random
        return (random.randrange(self.credit_min, self.credit_max))

    @property
    def interest(self):
        return self.interest

    @interest.setter
    def interest(self, principal_balance, apr, days):
        DAYS_IN_YEAR = 365
        self._interest = (self.principal_balance * (self.apr/DAYS_IN_YEAR) * self.days)

    @credit_line.setter
    def credit_line(self, value):
        self._credit_line = value

    @classmethod
    def random_number(self):
        import random
        return int(''.join(random.sample('01234567890123456789', 10)))

    @staticmethod
    def withdraw(credit_limit, amount):
        return credit_limit - amount
