from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import ExtUser
# Create your views here.


def home(request):
    role = ExtUser.objects.get(user = request.user.id).role()
    return render(request,'views/home.html',{'user':request.user, 'role':role})