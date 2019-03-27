from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Login page")

def encrpty(request):
    password = request.data['password']
    print (password)

    return
