from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .services import *

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            lending_service = LendingService()
            serializer.save()
        return Response(serializer.data)

class OpenAccountView(generics.CreateAPIView):
    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer

    def perform_create(self, serializer):
        serializer.save()

class WithdrawView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

class MakePaymentView(generics.ListCreateAPIView):
    pass

class TransactionsHistoryView(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
