from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):
    room_number = models.CharField(max_length=8,unique=True)
    room_type = models.CharField(max_length=30)
    seats = models.IntegerField(default=30)
    booked = models.IntegerField(blank=True, default=0)


    def __str__(self):
        return f'{self.room_number}({self.room_type})'

    class Meta:
        db_table = 'Room'



class Booking(models.Model):
    date = models.DateField(null = False )
    time_slot = models.CharField(max_length=20,default='')
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    reason = models.CharField(max_length=500,null=True)
    approval = models.BooleanField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'Booking'

    @property
    def faculty(self) -> str:
        '''Returns the name of the teacher who applied for the slot'''
        return self.user.username

    @property
    def room_number(self) -> str:
        '''Returns the room number and room type of booking'''
        return str(self.room)



class ApprovedTiming(models.Model):
    class Meta:
        db_table = 'Booked_timing'

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timinings = models.CharField(max_length=50)
    date = models.DateField()
    


# class TimeSlots(models.Model):
#     class Meta:
#         db_name = 'time_slots'
    
#     appliction = models.ForeignKey(Application, on_delete=models.CASCADE)
#     time = slot
    




