from django.urls import path
from django.conf.urls import url
from . import views
from dal import autocomplete

app_name = 'apps'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('pendaftaran/', views.PendaftaranView.as_view(), name='pendaftaran'),
    #path('pendaftaran/tambah', views.PendaftaranView.tambahpendaftaran, name='tambah-pendaftaran'),
    #path('pendaftaran/edit', views.PendaftaranView.editpendaftaran, name='edit-pendaftaran'),
    #path('pendaftaran/delete', views.deletependaftaran, name='delete-pendaftaran'),
    
]