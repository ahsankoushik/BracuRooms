from django.urls import path
from . import views

urlpatterns = [
    path('',views.Entrypoint.as_view(), name='api_entrypoint'),
    path('rooms', views.rooms, name='api_rooms' ),
    path('bookings', views.booking, name='api_booking'),
    path('get_booking_approval', views.get_booking_approval, name='api_get_booking_aproval'),
    path('approve/<int:id>/<int:flag>',views.approve, name='api_approve'),
    path('free_room',views.free_room, name='api_free_room'),
]