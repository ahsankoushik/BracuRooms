from django.contrib import admin

from .models import *

# Register your models here.


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','room_number','room_type')


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date','room')


class TeacherApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','user','room_number')

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('id','booking','timeslot')




admin.site.register(Room, RoomsAdmin)
admin.site.register(Booking, BookingsAdmin)
# admin.site.register(TeacherApplies,TeacherApplicationAdmin)
admin.site.register(TimeSlot,TimeSlotAdmin)
