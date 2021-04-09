from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<str:title>', views.gallery, name='gallery-filter'),
    path('chefs/', views.chefs, name='chefs'),

   
    
]