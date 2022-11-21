from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    room_number = models.CharField(max_length=8)
    room_type = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.room_number}({self.room_type})'

    class Meta:
        db_table = 'Room'




class Booking(models.Model):
    date = models.DateField(null = False )
    time_slot = models.IntegerField(null = False)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Bookings'



class ExtUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.BooleanField(default=False, null = True)
    teacher = models.BooleanField(default=False, null = True)
    admin = models.BooleanField(default= False, null= True)

    def role(self) -> str:
        '''Returns the role of the user'''
        r = 'set first'
        if self.student:r = 'student'
        if self.teacher: r = 'teacher' 
        if self.admin: r = 'admin'
        return r



    def is_admin(self) -> bool:
        '''Returns if the user is a admin or not'''
        return self.admin
    

    # def is_

    class Meta:
        db_table = 'ExtUser'




