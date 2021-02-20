from dal import autocomplete
from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker


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
        }

class SPPTLamaForm(forms.ModelForm):
    class Meta:
        model = SPPTLama
        fields= (
            'no_sppt_lama',
            'nama_wp_lama',
            'tarif_lama',
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
        }

class SPPTBaruForm(forms.ModelForm):
    class Meta:
        model = SPPTBaru
        fields= (
            'no_sppt_baru',
            'nama_wp_baru',
            'tarif_baru',
            'keterangan',
            'transaksi',
            'luas_tanah',
            'luas_bangunan',
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

            'transaksi':forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),

            'luas_tanah':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'luas_bangunan':forms.NumberInput(
                attrs={
                    'class':'form-control',
                }   
            ),
        }

class PendataanAutoForm(forms.ModelForm):
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
            )
        widgets =  {
            'tanggal_pendaftaran':DatePicker(
                attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'class':'form-control',
                'readonly':'',
                }
            ),

            'no_pelayanan':autocomplete.ListSelect2(
                url='selectnopel',
                attrs={
                    'class':'form-control col-sm-3',
                    'id' : 'pilih-nopel',
                    'data-placeholder' : 'Masukan No Pelayanan ...'
                }   
            ),
            'nama':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),
            'desa':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),
            'kecamatan':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),

            'mutasi':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),

            'jumlah':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),

            'keterangan':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                }
            ),

            'tanggal_selesai':DatePicker(
                attrs={
                    'class':'form-control',
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                    'readonly':'',
                }
            ),
        }