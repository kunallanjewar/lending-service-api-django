from rest_framework import permissions, generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, AccountDetailSerializer, TransactionSerializer
from .models import AccountDetail, Transaction
from .permissions import IsOwner
from django.contrib.auth.models import User

class CreateUserView(generics.CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class OpenAccountView(generics.ListCreateAPIView):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transaction
    #permission_classes = (permissions.IsAuthenticated, IsOwner)

    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)

class AccountDetailView(generics.ListAPIView):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetail
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class TransactionHistoryView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
