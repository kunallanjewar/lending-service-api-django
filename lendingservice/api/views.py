from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, AccountDetailSerializer, TransactionSerializer, RegisterSerializer
from .models import User as UserModel, AccountDetail, Transaction
from .permissions import IsOwner
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404


class RegisterAccountView(generics.CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class OpenAccountView(generics.CreateAPIView):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WithdrawView(generics.ListAPIView):
    pass

class MakePaymentView(generics.ListCreateAPIView):
    pass

class AccountDetailView(generics.ListAPIView):
    queryset = AccountDetail.objects.all()
    permission_classes = (AllowAny,)
    #permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = AccountDetail

class TransactionHistoryView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)
