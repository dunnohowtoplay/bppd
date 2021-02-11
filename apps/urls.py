from django.urls import path
from django.conf.urls import url
from . import views
from dal import autocomplete


urlpatterns = [
    path('', views.PendaftaranView.as_view(), name='pendaftaran'),


    url(
        'desa-autocomplete/$',
        views.DesaAutocomplete.as_view(),
        name='selectdesa',
    ),
    url(
        'kecamatan-autocomplete/$',
        views.KecamatanAutocomplete.as_view(),
        name='selectkecamatan',
    ),
]