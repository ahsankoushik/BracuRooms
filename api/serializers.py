from rest_framework import serializers
from django.contrib.auth.models import User
from rooms import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields ='__all__'



