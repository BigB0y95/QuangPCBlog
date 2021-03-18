from django.urls import path
from .import views

urlpatterns = {
    path('', views.index),
    path('Python', views.Python),
    path('BaiHoc', views.BaiHoc),
    path('TrangChu', views.TrangChu),
    path('GioiThieu', views.GioiThieu),
    path('DangNhap', views.DangNhap),
    path('DangKy', views.DangKy)
}