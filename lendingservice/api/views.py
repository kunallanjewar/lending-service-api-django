from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Profile, Account, Transaction
from .permissions import IsProfileOwner, IsAccountOwner, IsTransactionOwner
from django.contrib.auth.models import User
from .services import LendingService
from rest_framework.exceptions import APIException
from .serializers import(   ProfileSerializer, AccountSerializer,
                            TransactionSerializer, RegisterSerializer
                        )


class RegisterUserView(generics.CreateAPIView):
    """ Register a new user """
    model = User
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProfileView(generics.ListCreateAPIView):
    """ Get or Post user profile """
    permission_classes = (permissions.IsAuthenticated, IsProfileOwner)
    serializer_class = ProfileSerializer
    model = Profile

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except:
            raise APIException("Opps! There was a problem in creating your profile.")

    def get_queryset(self):
        try:
            return Profile.objects.filter(owner=self.request.user)
        except:
            raise APIException("Opps! There was a problem in retrieving your profile details.")

class AccountView(generics.ListCreateAPIView):
    """ Create Account or Get Account information """
    permission_classes = (permissions.IsAuthenticated, IsAccountOwner)
    serializer_class = AccountSerializer
    model = Account

    def perform_create(self, serializer):
        try:
            service = LendingService()
            serializer.save(    owner=self.request.user,
                                apr=service.apr,
                                credit_line=service.credit_line,
                                credit_limit=service.credit_line
                            )
        except:
            raise APIException("Opps! There was a problem in opening your credit account.")

    def get_queryset(self):
        try:
            return Account.objects.filter(owner=self.request.user)
        except:
            raise APIException("Opps! There was a problem in retrieving your credit account details.")

class TransactionView(generics.ListCreateAPIView):
    """ Get list of User transactions or Perform a Transaction """
    permission_classes = (permissions.IsAuthenticated, IsTransactionOwner)
    serializer_class = TransactionSerializer
    model = Transaction

    def perform_create(self, serializer):
        #try:
        from decimal import Decimal
        service = LendingService()
        if serializer.data['transaction_type'] == 'WDW':
            credit_line = Account.objects.filter(account_number=int(serializer.data['account']))
            print(credit_line.values('credit_line'))
            new_credit_limit = service.withdraw(500, Decimal(serializer.data['amount']))

        #serializer.save(owner=self.request.user)
        #except:
            #raise APIException("Opps! There was a problem in performing this transactions.")

    def get_queryset(self):
        try:
            return Transaction.objects.filter(owner=self.request.user)
        except:
            raise APIException("Opps! There was a problem in retrieving your transactions history.")
