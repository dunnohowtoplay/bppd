from dal import autocomplete
from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet


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
                'id':'tanggal_pendaftaran',
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
                    'id':'nama',
                }
            ),
            'desa':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                    'id':'desa',
                }
            ),
            'kecamatan':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                    'id':'kecamatan',
                }
            ),

            'mutasi':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                    'id':'mutasi',
                }
            ),

            'jumlah':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                    'id':'jumlah',
                }
            ),

            'keterangan':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'readonly':'',
                    'id':'keterangan',
                }
            ),

            'tanggal_selesai':DatePicker(
                attrs={
                    'class':'form-control',
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                    'readonly':'',
                    'id':'tanggal_selesai',
                }
            ),
        }

sppt_baru_formset = inlineformset_factory(SPPTLama, SPPTBaru, form=SPPTBaruForm, extra=1)
class BaseSpptFormset(BaseInlineFormSet):

    def add_fields(self, form, index):
        # allow the super class to create the fields as usual
        super(BaseSpptFormset, self).add_fields(form, index)

        # created the nested formset
        try:
            instance = self.get_queryset()[index]
            pk_value = instance.pk
        except IndexError:
            instance=None
            pk_value = hash(form.prefix)

        # store the formset in the .nested property
        form.nested = [
            sppt_baru_formset(data=self.data, instance = instance,prefix = "SPPTBaru_%s" % pk_value)]
    
    def is_valid(self):
        result = super(BaseSpptFormset, self).is_valid()

        for form in self.forms:
            if hasattr(form, "nested"):
                for n in form.nested:
                    # make sure each nested formset is valid as well
                    result = result and n.is_valid()

        return result
    
    def save_new(self, form, commit=True):
        """Saves and returns a new model instance for the given form."""

        instance = super(BaseSpptFormset, self).save_new(form, commit=commit)

        # update the form’s instance reference
        form.instance = instance

        # update the instance reference on nested forms
        for nested in form.nested:
            nested.instance = instance

            # iterate over the cleaned_data of the nested formset and update the foreignkey reference
            for cd in nested.cleaned_data:
                cd[nested.fk.name] = instance

        return instance

    def should_delete(self, form):
        """Convenience method for determining if the form’s object will
        be deleted; cribbed from BaseModelFormSet.save_existing_objects."""

        if self.can_delete:
            raw_delete_value = form._raw_value(DELETION_FIELD_NAME)
            should_delete = form.fields[DELETION_FIELD_NAME].clean(raw_delete_value)
            return should_delete

        return False

    def save_all(self, commit=True):
        """Save all formsets and along with their nested formsets."""

        # Save without committing (so self.saved_forms is populated)
        # — We need self.saved_forms so we can go back and access
        #    the nested formsets
        objects = self.save(commit=False)

        # Save each instance if commit=True
        if commit:
            for o in objects:
                o.save()

        # save many to many fields if needed
        if not commit:
            self.save_m2m()

        # save the nested formsets
        for form in set(self.initial_forms + self.saved_forms):
            if self.should_delete(form): continue

            for nested in form.nested:
                nested.save(commit=commit)

