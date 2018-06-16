from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from .serializers import *
from .models import *
from .services import *

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

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

class TransactionsHistoryView(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Transactions.objects.all()
        transactions = get_object_or_404(queryset, pk=pk)
        serializer = TransactionsSerializer(transactions)
        return Response(serializer.data)

transactions_list = TransactionsHistoryView.as_view({
    'get': 'list',
    'post': 'create'
})

details = TransactionsHistoryView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
router = DefaultRouter()
router.register(r'^api/transactions/$',
                                TransactionsHistoryView,
                                base_name='transactions'
                            )
