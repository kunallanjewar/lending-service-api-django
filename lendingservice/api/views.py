from django.shortcuts import render
from rest_framework import permissions, generics, status, viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from .serializers import UserSerializer, AccountDetailSerializer, TransactionSerializer
from .models import User as UserModel, AccountDetail, Transaction

class CreateUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,) 

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class OpenAccountView(generics.CreateAPIView):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WithdrawView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class MakePaymentView(generics.ListCreateAPIView):
    pass

class AccountDetailView(generics.ListAPIView):
    queryset = AccountDetail.objects.all()
    serializer_class = AccountDetail

class TransactionHistoryView(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Transaction.objects.all()
        transactions = get_object_or_404(queryset, pk=pk)
        serializer = TransactionSerializer(transactions)
        return Response(serializer.data)
