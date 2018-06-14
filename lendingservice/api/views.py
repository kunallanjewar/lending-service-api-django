from django.shortcuts import render
from rest_framework import generics
from .serializers import Serializer
from .models import User

class CreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Serializer()

    def create(self, serializer):
        serializer.save()
