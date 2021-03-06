from dal import autocomplete
from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker
from djangoformsetjs.utils import formset_media_js

class PendaftaranForm(forms.ModelForm):
    class Meta:
        model=Pendaftaran
        fields= (
            'tanggal_pendaftaran',
            'no_pelayanan',
            'nama',
            'desa',
            'kecamatan',
            'mutasi',
            'jumlah',
            'keterangan',
            'tanggal_selesai',
            'kontak',
            )
        widgets =  {
            'tanggal_pendaftaran':DatePicker(
                attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                }
            ),

            'no_pelayanan':forms.TextInput(
                attrs={
                    'class':'form-control disabled',
                    'readonly':'',
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
                    'data-placeholder': 'Desa ...',
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

            'jumlah':forms.NumberInput(
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
            'kontak':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
        }

class SPPTLamaForm(forms.ModelForm):
    class Media(object):
        js = formset_media_js

    class Meta:
        model = SPPTLama
        fields= (
            'no_sppt_lama',
            'nama_wp_lama',
            'tarif_lama',
            'luas_tanah_lama',
            'luas_bangunan_lama',
            )
        widgets =  {
            'no_sppt_lama':forms.TextInput(
                attrs={
                    'class':'form-control',
                }   
            ),

            'nama_wp_lama':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'tarif_lama':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'luas_tanah_lama':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'luas_bangunan_lama':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }   
            ),
        }

class SPPTBaruForm(forms.ModelForm):
    class Media(object):
        js = formset_media_js
        
    class Meta:
        model = SPPTBaru
        fields= (
            'no_sppt_baru',
            'nama_wp_baru',
            'tarif_baru',
            'keterangan',
            'transaksi',
            'luas_tanah_baru',
            'luas_bangunan_baru',
            )
        widgets =  {
            'no_sppt_baru':forms.TextInput(
                attrs={
                    'class':'form-control',
                }   
            ),

            'nama_wp_baru':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'tarif_baru':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'keterangan':forms.Select(
                attrs={
                    'class':'form-control',
                }   
            ),

            'transaksi':forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),

            'luas_tanah_baru':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'luas_bangunan_baru':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }   
            ),
        }