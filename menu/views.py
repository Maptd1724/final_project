from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu
from chefs.models import Chef
from gallery.models import Gallery



def index(request):
    menu = Menu.objects.order_by('price').filter(is_published=True)

    context = {
        'menu': menu
    }

    return render(request, 'menu/menu.html', context)

def chefs(request):
    # Get chef
    chefs = Chef.objects.order_by('name')

    context = {
        'chefs': chefs
    }

    return render(request, 'menu/chef.html', context)

def gallery(request, title=None):
    if title == None:
        photos = Gallery.objects.all()
    
    else:
        photos = Gallery.objects.filter(title=title.capitalize())

    context = {
        'photos': photos,
       
        
    }

    return render(request, 'menu/gallery.html', context=context)
