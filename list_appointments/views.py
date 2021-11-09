from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from list_appointments.models import RolesUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@login_required
def index (request):
     return render(request, 'index.html',{})


@login_required
def list_patients(request):
    users = RolesUser.objects.all() #conectar a la base de datos
    return render(request, 'list_appointments/list.html',{'roles_user': users})


def login_view(request):
    if request.method == 'POST':
        username = request.POST[ 'username']
        password = request.POST[ 'password']

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            return render(request, 'login.html',{'error':'Username or password incorrect'})
    return render(request,'login.html',{})

def regist(request):
    return render(request, 'regist.html',{})


def listado(request):
    lista = serializers.serialize('jason', RolesUser.objects.all() )
    return HttpResponse(lista, content_type = 'application/json')
 


    
