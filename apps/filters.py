import django_filters
from django import forms
from .models import Pendaftaran

class NoPendaftaranFilter(django_filters.FilterSet):
    no_pelayanan = django_filters.CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control me-2 rounded',
                'placeholder': 'Search No pelayanan',
            }
        )
    )

    class Meta:
        model = Pendaftaran
        fields = ['no_pelayanan']