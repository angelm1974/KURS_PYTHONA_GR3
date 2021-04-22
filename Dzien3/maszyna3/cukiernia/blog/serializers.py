from django.contrib.auth.models import User
from rest_framework import serializers


class PytanieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        field = ['username', 'email', 'firstname', 'lastname']
