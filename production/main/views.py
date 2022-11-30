from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')