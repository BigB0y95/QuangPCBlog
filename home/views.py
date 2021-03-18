from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def Python(request):
    return render(request, 'pages/subjects.html')
def BaiHoc(request):
    return render(request, 'pages/lesson.html')
def TrangChu(request):
    return render(request, 'pages/home.html')
def GioiThieu(request):
    return render(request, 'pages/about.html')
def DangNhap(request):
    return render(request, 'pages/sign_in.html')
def DangKy(request):
    return render(request, 'pages/register.html')