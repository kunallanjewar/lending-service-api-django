from .models import Profile, Account, Transaction

class LendingService(object):

    def __init__(self,
                credit_min=500,
                credit_max=5000,
                apr_min=0.05,
                apr_max=0.35):

        self.credit_min = credit_min
        self.credit_max = credit_max
        self.apr_min = apr_min
        self.apr_max = apr_max

    @property
    def apr(self):
        return self.apr_max

    @property
    def credit_line(self):
        return self.credit_max

    @property
    def random_apr(self):
        import random
        return (random.randrange(apr_min*100, apr_max*100))/100

    @property
    def random_credit_line(self):
        import random
        return (random.randrange(credit_min*100, credit_max*100))/100
