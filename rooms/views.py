from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
# Create your views here.




@login_required
def home(request):

    return render(request,'views/home.html',{})


@login_required
def apply(request):

    return render(request, 'views/apply.html', {'total':Booking.objects.all().count()} )


@login_required
def rooms(request):

    return render(request, 'views/rooms.html', {} )