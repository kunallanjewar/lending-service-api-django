from rest_framework import permissions, generics, status, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, AccountDetailSerializer, TransactionSerializer
from .models import User as UserModel, AccountDetail, Transaction
from .permissions import IsOwner

class CreateUserView(generics.ListCreateAPIView):
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
    serializer_class = AccountDetail
    permission_classes = (permissions.IsAuthenticated, IsOwner)

class TransactionHistoryView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
