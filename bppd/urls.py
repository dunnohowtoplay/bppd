"""bppd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dal import autocomplete
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from apps import views
from users import views as uv

urlpatterns = [
    #url(
    #    'nopel-autocomplete/$',
    #    views.NopelAutocomplete.as_view(),
    #    name='selectnopel',
    #),
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
    path('admin/', admin.site.urls),
    path('register/', uv.registerPage, name="register"),
    path('login/', uv.loginPage, name="login"),
    path('logout/', uv.logoutPage, name="logout"),
    path('', include('apps.urls')),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)