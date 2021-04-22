from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import PytanieSerializer


class PytanieApi(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = PytanieSerializer
    permission_classes = [permissions.IsAuthenticated]
