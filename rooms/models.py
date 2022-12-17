from django.db import models

# Create your models here.
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


'''
CREATE TABLE `Room` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `room_number` varchar(8) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `seats` int NOT NULL,
  `booked` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `room_number` (`room_number`)
) 
'''





class Booking(models.Model):
    date = models.DateField(null = False )
    # time_slot = models.CharField(max_length=20,default='')
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    reason = models.CharField(max_length=500,null=True)
    approval = models.BooleanField(null=True)
    approver = models.ForeignKey(User, on_delete= models.CASCADE, null = True, related_name='approver')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='applier')

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

    @property
    def id_room(self) -> str:
        '''Return the id of the room'''
        return self.room.id




'''
CREATE TABLE `Booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `reason` varchar(500) DEFAULT NULL,
  `approval` tinyint(1) DEFAULT NULL,
  `approver_id` int DEFAULT NULL,
  `room_id` bigint NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`approver_id`) REFERENCES `auth_user` (`id`),
  FOREIGN KEY (`room_id`) REFERENCES `Room` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) 
'''





class TimeSlot(models.Model):
    class Meta:
        db_table = 'time_slot'
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,null=False)
    timeslot = models.IntegerField()


'''
CREATE TABLE `time_slot` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `timeslot` int NOT NULL,
  `booking_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`booking_id`) REFERENCES `Booking` (`id`)
) 
'''



class RequestsForSeats(models.Model):
    class Meta:
        db_table = 'seat_request'
    user = models.ForeignKey(User,on_delete= models.CASCADE,null = True)
    Room_number = models.ForeignKey(Room,on_delete=models.CASCADE,blank= True,null= True)
    seats_requested = models.BooleanField(blank= True,default =0,null=True)


'''
CREATE TABLE `seat_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `seats_requested` tinyint(1) DEFAULT NULL,
  `Room_number_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`Room_number_id`) REFERENCES `Room` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
)
'''



# class ApprovedTiming(models.Model):
#     class Meta:
#         db_table = 'Booked_timing'

#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     timinings = models.CharField(max_length=50)
#     date = models.DateField()
    

# # class user(models.Model):
# #     class Meta:
# #         db_name ='user'
# #     username = models.CharField(max_length=10,unique = True)
# #     name = models.CharField(max_length=128)
# #     email = models.CharField(max_lengh=30)
# #     password = models.CharField(max_lengh=4)
        

# class AdminApproves(models.Model):
#     class Meta:
#         db_table = 'approval'
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
#     room_number = models.ForeignKey(Room,on_delete = models.CASCADE) 
#     approval = models.BooleanField(null=True)

# class TeacherApplies(models.Model):
#     class Meta:
#         db_table = 'application'
#     user = models.ForeignKey(User,on_delete =models.CASCADE,null = True )
#     room_number = models.ForeignKey(Room,on_delete = models.CASCADE)



# class TimeSlots(models.Model):
#     class Meta:
#         db_name = 'time_slots'
    
#     appliction = models.ForeignKey(Application, on_delete=models.CASCADE)
#     time = slot
    