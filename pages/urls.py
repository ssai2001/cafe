# header file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'), 
    path('contactUs/', views.contactUs, name='contactUs'),
]