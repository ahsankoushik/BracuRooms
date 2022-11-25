from django.urls import path
from . import views

urlpatterns = [
    path('',views.Entrypoint.as_view(), name='api_entrypoint'),
    path('rooms', views.rooms, name='api_rooms' ),
    path('bookings', views.booking, name='api_booking'),

]