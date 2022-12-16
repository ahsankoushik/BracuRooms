from django.urls import path
from . import views

urlpatterns = [
    path('',views.Entrypoint.as_view(), name='api_entrypoint'),
    path('rooms', views.rooms, name='api_rooms' ),
    path('bookings', views.booking, name='api_booking'),
    path('get_booking_approval', views.get_booking_approval, name='api_get_booking_aproval'),
    path('approve/<int:id>/<int:flag>',views.approve, name='api_approve'),
    path('free_room_teacher',views.free_room_teacher, name='api_free_room_teacher'),
    path('free_room_st',views.free_room_st, name='api_free_room_st'),


    path('book_a_seat/<int:room>',views.book_a_seat, name= 'api_book_a_seat'),
    path('remove_seat',views.remove_seat, name='api_remove_seat')
]