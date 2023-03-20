from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    return render(request,'pages/index.html')

def aboutUs(request):
    students = {'Tom':80,'Jerry':45,'casper':65,'Droopy':32}
    context={
        'student':students, 
    }
    return render(request,'pages/about.html',context)

def contactUs(request):
    return render(request,'pages/contact.html')