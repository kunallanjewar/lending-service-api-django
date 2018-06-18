from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Profile, Account, Transaction
from .permissions import IsOwner, IsUserHimself
from django.contrib.auth.models import User
from .serializers import(   ProfileSerializer, AccountSerializer,
                            TransactionSerializer, RegisterSerializer
                        )

class RegisterAccountView(generics.CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProfileView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = ProfileSerializer
    model = Profile

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(owner=self.request.user)

class AccountView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AccountSerializer
    model = Account

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)

class TransactionView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)

class WithdrawView(generics.ListAPIView):
    pass

class MakePaymentView(generics.ListCreateAPIView):
    pass
