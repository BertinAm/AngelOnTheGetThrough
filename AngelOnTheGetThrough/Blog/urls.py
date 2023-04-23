from django.urls import path
from . import views

# creating the first path with route set empty strings , with view set to views.home and name set to Blog-home
urlpatterns = [
    path('', views.home, name='Blog-home')
]
