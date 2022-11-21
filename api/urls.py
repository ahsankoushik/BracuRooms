from django.urls import path
from . import views

urlpatterns = [
    path('',views.Entrypoint.as_view(), name='entrypoint'),
    

]