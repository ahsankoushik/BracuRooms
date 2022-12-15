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


class BookingApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ['id', 'faculty','room_number','date']


class BookingAddSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ['date','room','reason']
