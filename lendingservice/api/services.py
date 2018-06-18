
class LendingService(object):

    def __init__(self,
                credit_min=500,
                credit_max=5000,
                apr=0.35,
                interest=0.0,
                principal_balance=0.0):

        self.credit_min = credit_min
        self.credit_max = credit_max
        self.apr = apr
        self.interest =

    @property
    def apr_fixed(self):
        return self.apr

    @property
    def credit_line(self):
        return self.credit_max

    @property
    def random_credit_line(self):
        import random
        return (random.randrange(credit_min*100, credit_max*100))/100

    @property
    def random_number(self):
        import random
        return int(''.join(random.sample('01234567890123456789', 10)))

    @property
    def interest(self):
        return self.interest

    @interest.setter
    def interest(self, principal_balance, apr, days):
        DAYS_IN_YEAR = 365
        self.interest = (principal_balance * (apr/DAYS_IN_YEAR) * days)
