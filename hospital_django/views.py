from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request,'index.html')

def aboutUS(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')

def department(request):
    return render(request,'department.html')