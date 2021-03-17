from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def python_page(request):
    return render(request, 'pages/python_page.html')
def home(request):
    return render(request, 'pages/home.html')
def about(request):
    return render(request, 'pages/about.html')