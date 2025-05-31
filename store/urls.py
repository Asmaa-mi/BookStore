from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index.html', views.home, name='home'),
    path('Project2.html', views.Project2, name='project2'),
    path('Project3.html', views.Project3, name='project3'),
    path('Project4.html', views.Project4, name='project4'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),


]

