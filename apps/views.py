from dal import autocomplete
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string
from .filters import NoPendaftaranFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import inlineformset_factory


class DesaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Desa.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs

class KecamatanAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Kecamatan.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs

class NopelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Pendaftaran.objects.all()

        if self.q:
            qs = qs.filter(no_pelayanan__istartswith=self.q)

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
def pendataan_view(request):
    data_daftars = Pendaftaran.objects.all()
    sppt_lamas = SPPTLama.objects.all().order_by('no_pelayanan')
    sppt_barus = SPPTBaru.objects.all().order_by('sppt_lama__no_pelayanan')
    form_spptlama = SPPTLamaForm()
    form_spptbaru = SPPTBaruForm()
    form_data = PendataanAutoForm()
    context = {
        'data_daftars':data_daftars,
        'sppt_lamas':sppt_lamas,
        'sppt_barus':sppt_barus,
        'form_spptlama':form_spptlama,
        'form_spptbaru':form_spptbaru,
        'form_data':form_data,
        }
    return render(request, 'apps/pendataan.html', context)


def pendataan_create(request):
    sppt_lama_formset = inlineformset_factory(Pendaftaran, SPPTLama, form=SPPTLamaForm, max_num=2)
    sppt_baru_formset = inlineformset_factory(SPPTLama, SPPTBaru, form=SPPTBaruForm, max_num=2)
    #no_pel = Pendaftaran.objects.get(no_pelayanan=no_p)
    #no_slama = SPPTLama.objects.get(no_sppt_lama=no_sl)
    sl_formset = sppt_lama_formset(prefix='spptlama')
    sb_formset = sppt_baru_formset(prefix='spptbaru')
    form_spptlama = SPPTLamaForm()
    form_spptbaru = SPPTBaruForm()
    form_data = PendataanAutoForm()
    context = {
        'sl_formset':sl_formset,
        'sb_formset':sb_formset,
        'form_spptlama':form_spptlama,
        'form_spptbaru':form_spptbaru,
        'form_data':form_data,
        }
    return render(request, 'apps/create_pendataan.html', context)

def autofill_pendataan(request):
    data = dict()
    if request.method == 'GET' and request.is_ajax():
        data_id = request.GET.get('noPel', None)
        no_pel = Pendaftaran.objects.get(id=data_id)
        data['tanggal_pendaftaran'] = no_pel.tanggal_pendaftaran
        data['no_pelayanan'] = no_pel.no_pelayanan
        data['nama'] = no_pel.nama
        data['desa'] = no_pel.desa.nama
        data['kecamatan'] = no_pel.kecamatan.nama
        data['mutasi'] = no_pel.mutasi
        data['jumlah'] = no_pel.jumlah
        data['keterangan'] = no_pel.keterangan
        data['tanggal_selesai'] = no_pel.tanggal_selesai

        return JsonResponse({"data_pendaftaran":data})