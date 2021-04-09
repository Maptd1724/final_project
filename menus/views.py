from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'menus/index.html')
    
def about(request):
    return render(request, 'menus/about.html')

def services(request):
    return render(request, 'menus/services.html')
