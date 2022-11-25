from rest_framework import serializers
from django.contrib.auth.models import User
from rooms import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields ='__all__'

class BookingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'


class BookingAddSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ['date','room','time_slot','reason']
