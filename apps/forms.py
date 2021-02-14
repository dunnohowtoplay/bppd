from dal import autocomplete
from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker


class PendaftaranForm(forms.ModelForm):
    desa = forms.ModelChoiceField(
        queryset=Desa.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='selectdesa',
            attrs={
                'class':'form-control',
                'id':'pilihdesa',
                'data-placeholder': 'Desa ...',
                })
    )
    class Meta:
        model=Pendaftaran
        fields= (
            'tanggal_pendaftaran',
            'nama',
            'desa',
            'kecamatan',
            'mutasi',
            'jumlah',
            'keterangan',
            'tanggal_selesai',
            )
        widgets =  {
            'tanggal_pendaftaran':DatePicker(
                attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                }
            ),

            'nama':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'kecamatan':autocomplete.ModelSelect2(
                url='selectkecamatan',
                attrs={
                    'class':'form-control',
                    'id':'pilihkecamatan',
                    'data-placeholder': 'Kecamatan ...',
                }
            ),

            'mutasi':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'jumlah':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'keterangan':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),

            'tanggal_selesai':DatePicker(
                attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                }
            ),
        }

