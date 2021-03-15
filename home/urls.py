from django.urls import path
from .import views

urlpatterns = {
    path('', views.index),
    path('python_page', views.python_page),
    path('home', views.home)
}