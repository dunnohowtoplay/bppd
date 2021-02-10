from django.shortcuts import render, redirect
from .models import *
from .forms import PendaftaranForm
from django.http import JsonResponse
from dal import autocomplete


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

app_name = 'apps'
def index(request):
    desas = Desa.objects.all()
    kecamatans = Kecamatan.objects.all()
    datas = Pendaftaran.objects.all()
    form = PendaftaranForm()

    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(index)
    '''
    if 'term' in request.GET:
        qsdesa = Desa.objects.filter(nama__icontains=request.GET.get('term'))
        listdesa = list()
        for x in qsdesa:
            listdesa.append(x.nama)
        return JsonResponse(listdesa, safe=False)
    '''
    context = {
        'datas':datas,
        'desas':desas,
        'kecamatans':kecamatans,
        'form':form,
        }
    

    return render(request, 'apps/index.html', context)