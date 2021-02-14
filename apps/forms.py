from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker
from dal import autocomplete

class PendaftaranForm(forms.ModelForm):
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

            'desa':autocomplete.ModelSelect2(
                url='selectdesa',
                attrs={
                    'class':'form-control',
                    'id':'pilihdesa',
                    
                }
            ),

            'kecamatan':autocomplete.ModelSelect2(
                url='selectkecamatan',
                attrs={
                    'class':'form-control',
                    'id':'pilihkecamatan'
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
'''
class EditPendaftaranForm(forms.ModelForm):
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

            'desa':autocomplete.ModelSelect2(
                url='selectdesa',
                attrs={
                    'class':'form-control',
                    'id':'pilihdesa',
                    
                }
            ),

            'kecamatan':autocomplete.ModelSelect2(
                url='selectkecamatan',
                attrs={
                    'class':'form-control',
                    'id':'pilihkecamatan'
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
   ''' 
