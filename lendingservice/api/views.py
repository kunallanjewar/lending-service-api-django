from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Profile, Account, Transaction
from .permissions import IsOwner, IsUserHimself
from django.contrib.auth.models import User
from .services import LendingService
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
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = ProfileSerializer
    model = Profile

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)

class AccountView(generics.ListCreateAPIView):
    """ Create Account or Get Account information """
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AccountSerializer
    model = Account

    def perform_create(self, serializer):
        apr = LendingService().apr
        credit_line = LendingService().credit_max

        serializer.save(    owner=self.request.user,
                            apr=apr,
                            credit_line=credit_line
                        )

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

class TransactionView(generics.ListAPIView):
    """ Get list of User transactions """
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)

class WithdrawView(generics.ListAPIView):
    pass

class MakePaymentView(generics.ListCreateAPIView):
    pass
