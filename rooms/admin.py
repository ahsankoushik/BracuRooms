from django.contrib import admin

from .models import *

# Register your models here.


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','room_number','room_type','seats','booked')


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date','room','approval')


class TeacherApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','user','room_number')

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id','booking','timeslot')

class SeatRequestAdmin(admin.ModelAdmin):
    list_display = ('id','user','Room_number','seats_requested')




admin.site.register(Room, RoomsAdmin)
admin.site.register(Booking, BookingsAdmin)
# admin.site.register(TeacherApplies,TeacherApplicationAdmin)
admin.site.register(TimeSlot,TimeSlotAdmin)
admin.site.register(RequestsForSeats,SeatRequestAdmin)
