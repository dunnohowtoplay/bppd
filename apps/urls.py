from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'apps'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('pendaftaran/', views.daftar_list, name='pendaftaran'),
    path('pendaftaran/tambah', views.daftar_create, name='daftar_create'),
    path('pendaftaran/<no_pelayanan>/edit', views.daftar_update, name='daftar-update'),
    path('pendaftaran/delete', views.daftar_delete, name='daftar-delete'),
    path('pendataan/', views.Pendataan_view, name='pendataan'),
    
]