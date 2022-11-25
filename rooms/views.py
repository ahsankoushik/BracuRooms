from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ExtUser
# Create your views here.

@login_required
def home(request):
    try:
        u = ExtUser.objects.get(user = request.user.id)
        role = u.role()
    except:
        role = 'set role first'
    return render(request,'views/home.html',{'user':request.user, 'role':role})


@login_required
def apply(request):
    u = ExtUser.objects.get(user = request.user.id)

    return render(request, 'views/apply.html', {'teacher':u.is_teacher(),'admin':u.is_admin()})