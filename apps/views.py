from dal import autocomplete
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PendaftaranForm
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string


class DesaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Desa.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q).order_by('nama')

        return qs

class KecamatanAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Kecamatan.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs

class Home(View):
    template_name = 'apps/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def daftar_list(request):
    datas = Pendaftaran.objects.all()
    form = PendaftaranForm()
    context = {
        'datas': datas,
        'form':form
        }
    return render(request, 'apps/pendaftaran.html',context)

def save_all(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            datas = Pendaftaran.objects.all()
            data['daftar_list'] = render_to_string('apps/daftar_list.html',{'datas':datas})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form
        }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def daftar_create(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
    else:
        form = PendaftaranForm()
    return save_all(request,form,'apps/create_daftar.html')

def Pendataan_view(request):
    form=PendaftaranForm()
    context = {'form':form}
    return render(request, 'apps/pendataan.html', context)


def daftar_update(request,id):
	data_id = get_object_or_404(Pendaftaran,id=id)
	if request.method == 'POST':
		form = BookForm(request.POST,instance=data_id)
	else:
		form = BookForm(instance=data_id)
	return save_all(request,form,'apps/update_daftar.html')

def daftar_delete(request):
    if request.method == "POST":
        data_ids = request.POST.getlist('deleteid[]')
        for id in data_ids:
            x = Pendaftaran.objects.get(pk=id)
            print(x)
            x.delete()

        return redirect('apps:pendaftaran')

