from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PendaftaranForm
from django.http import JsonResponse
from dal import autocomplete
from django.views.generic import View

app_name = 'apps'
class DesaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated:
            #return Desa.objects.none()

        qs = Desa.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs

class KecamatanAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated:
            #return Desa.objects.none()

        qs = Kecamatan.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs

class PendaftaranView(View):
    def get(self, request, *args, **kwargs):
        datas= Pendaftaran.objects.all()
        desas = Desa.objects.all()
        kecamatans = Kecamatan.objects.all()
        form = PendaftaranForm()
        context = {
            'desas':desas,
            'kecamatans':kecamatans,
            'datas':datas,
            'form':form,
            }

        return render(request, 'apps/index.html', context)

    def post(self, request, *args, **kwargs):
        datas=Pendaftaran.objects.all()
        desas = Desa.objects.all()
        kecamatans = Kecamatan.objects.all()
        context = {
            'datas':datas,
            'desas':desas,
            'kecamatans':kecamatans,
            'datas':datas,
            }

        if request.method == "POST":
            tambahform = PendaftaranForm(request.POST)
            #editdataid = request.POST.get('editid')
            #editdata = get_object_or_404(Pendaftaran, id = editdataid)
            #print(editdata)
            #editform = PendaftaranForm(request.POST or None, instance=editdata)
            data_ids=request.POST.getlist('deleteid[]')
            if tambahform.is_valid():
                tambahform.save()

            #if editform.is_valid():
                #editform.save()

            for id in data_ids:
                x = Pendaftaran.objects.get(pk=id)
                print(x)
                x.delete()
            
            return redirect('pendaftaran')
        
        return render(request, 'apps/index.html', context)
    
        

