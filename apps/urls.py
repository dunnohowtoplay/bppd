from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'apps'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    #pendaftaran
    path('pendaftaran/', views.daftar_list, name='pendaftaran'),
    path('pendaftaran/create', views.daftar_create, name='daftar_create'),
    path('pendaftaran/<no_pelayanan>/edit', views.daftar_update, name='daftar-update'),
    path('pendaftaran/delete', views.daftar_delete, name='daftar-delete'),

    #pendataan
    path('pendataan/', views.pendataan_view, name='pendataan'),
    path('pendataan/create', views.pendataan_create, name='pendataan_create'),
    path('pendataan/autofill', views.autofill_pendataan, name='autofill_pendataan'),
    path('pendataan/createformset/<int:id>', views.edit_sppt, name='createformset'),
    
]