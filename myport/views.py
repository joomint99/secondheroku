from django.shortcuts import render
from .models import Myport
# Create your views here.

def myport(request):
    myports=Myport.objects
    return render(request,'myport.html',{'myports':myports})

