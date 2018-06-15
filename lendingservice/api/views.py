from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

class CreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
