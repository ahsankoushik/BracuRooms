from django.contrib import admin

from .models import Room, Booking

# Register your models here.


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','room_number','room_type')


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date','time_slot','room','approval')





admin.site.register(Room, RoomsAdmin)
admin.site.register(Booking, BookingsAdmin)
