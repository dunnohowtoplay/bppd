from dal import autocomplete
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from .filters import NoPendaftaranFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

#Pendaftaran function
def daftar_list(request):
    datas = Pendaftaran.objects.all().order_by('no_pelayanan')
    form = PendaftaranForm()
    filtered = NoPendaftaranFilter(request.GET, queryset=datas)
    f = NoPendaftaranFilter(request.GET, queryset=datas).qs
    paginator = Paginator(f, 10)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    context = {
        'datas': datas,
        'form':form,
        'filter' : f,
        'filtered':filtered,
        'pages' : pages,
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


def daftar_update(request, no_pelayanan):
    dataid= Pendaftaran.objects.get(no_pelayanan=no_pelayanan)
    print(dataid)
    if request.method == 'POST':
        form = PendaftaranForm(request.POST,instance=dataid)
    else:
        form = PendaftaranForm(instance=dataid)
    return save_all(request,form,'apps/update_daftar.html')

def daftar_delete(request):
    if request.method == "POST":
        data_ids = request.POST.getlist('deleteid[]')
        for no_pelayanan in data_ids:
            x = Pendaftaran.objects.get(no_pelayanan=no_pelayanan)
            print(x)
            x.delete()

        return redirect('apps:pendaftaran')

#Pendataan Function
def Pendataan_view(request):
    data_daftars = Pendaftaran.objects.all()
    sppt_lamas = SPPTLama.objects.all().order_by('no_pelayanan')
    sppt_barus = SPPTBaru.objects.all().order_by('sppt_lama__no_pelayanan')
    form_spptlama = SPPTLamaForm()
    form_spptbaru = SPPTBaruForm()
    context = {
        'data_daftars':data_daftars,
        'sppt_lamas':sppt_lamas,
        'sppt_barus':sppt_barus,
        'form_spptlama':form_spptlama,
        'form_spptbaru':form_spptbaru,
        }
    return render(request, 'apps/pendataan.html', context)