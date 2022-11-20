from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Rooms(models.Model):
    room_number = models.CharField(max_length=8)
    room_type = models.CharField(max_length=30)




class Bookings(models.Model):
    date = models.DateField(null = False )
    time_slot = models.IntegerField(null = False)
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)


class ExtUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.BooleanField(default=False, null = True)
    teacher = models.BooleanField(default=False, null = True)
    admin = models.BooleanField(default= False, null= True)
    



