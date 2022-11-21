from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(request):
    return render(request,'index.html')

def tablets(request):
    return render(request,'brief.html')

def cough(request):
    return render(request,'cough.html')

def xyz(request):
    return render(request,'xyz.html')
