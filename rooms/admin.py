from django.contrib import admin

from .models import Room, Booking, ExtUser

# Register your models here.


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','room_number','room_type')


class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id','date','time_slot','room')


class ExtUserAdmin(admin.ModelAdmin):
    list_display = ('id','user','student','teacher','admin')



admin.site.register(Room, RoomsAdmin)
admin.site.register(Booking, BookingsAdmin)
admin.site.register(ExtUser, ExtUserAdmin)