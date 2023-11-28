from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'login.html')

def Cc(request):
    return render(request,'color.html')

def im(request):
    return render(request,'photos.html')