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
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from users.decorators import admin_only


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
@login_required(login_url='login')
def daftar_list(request):
    datas = Pendaftaran.objects.all().order_by('no_pelayanan')
    form = PendaftaranForm()
    filtered = NoPendaftaranFilter(request.GET, queryset=datas)
    is_admin = request.user.groups.filter(name='admin').exists()
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
        'is_admin': is_admin,
        }
    return render(request, 'apps/pendaftaran.html',context)

@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@admin_only
def daftar_create(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
    else:
        form = PendaftaranForm()
    return save_all(request,form,'apps/create_daftar.html')

@login_required(login_url='login')
@admin_only
def daftar_update(request, no_pelayanan):
    dataid= Pendaftaran.objects.get(no_pelayanan=no_pelayanan)
    print(dataid)
    if request.method == 'POST':
        form = PendaftaranForm(request.POST,instance=dataid)
    else:
        form = PendaftaranForm(instance=dataid)
    return save_all(request,form,'apps/update_daftar.html')

@login_required(login_url='login')
@admin_only
def daftar_delete(request):
    if request.method == "POST":
        data_ids = request.POST.getlist('deleteid[]')
        for no_pelayanan in data_ids:
            x = Pendaftaran.objects.get(no_pelayanan=no_pelayanan)
            print(x)
            x.delete()

        return redirect('apps:pendaftaran')

#Pendataan Function
@login_required(login_url='login')
def pendataan_view(request):
    data_daftars = Pendaftaran.objects.all().order_by('no_pelayanan')
    sppt_lamas = SPPTLama.objects.all()
    sppt_barus = SPPTBaru.objects.all()
    filtered = NoPendaftaranFilter(request.GET, queryset=data_daftars)
    f = NoPendaftaranFilter(request.GET, queryset=data_daftars).qs
    paginator = Paginator(f, 10)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    
    context = {
        'data_daftars':data_daftars,
        'sppt_lamas':sppt_lamas,
        'sppt_barus':sppt_barus,
        'filter' : f,
        'filtered':filtered,
        'pages' : pages,
        }
    return render(request, 'apps/pendataan.html', context)

'''json autofill form
def autofill_pendataan(request):
    data = dict()
    if request.method == 'GET' and request.is_ajax():
        data_id = request.GET.get('noPel', None)
        if data_id == '':
            pass
        else:
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
'''

@login_required(login_url='login')
@admin_only
def manage_sppt_lama(request, no_pelayanan):
    noPel = Pendaftaran.objects.get(no_pelayanan=no_pelayanan)
    SpptLamaInlineFormSet = inlineformset_factory(Pendaftaran, SPPTLama, form=SPPTLamaForm, extra=0)
    formset = SpptLamaInlineFormSet(instance=noPel)
    if request.method == "POST":
        formset = SpptLamaInlineFormSet(request.POST, instance=noPel)
        if formset.is_valid():
            formset.save()
            print('success')
            # Do something. Should generally end with a redirect. For example:
            return redirect('/pendataan')
        else:
            print('ERROR', formset.errors)
    else:
        formset = SpptLamaInlineFormSet(instance=noPel)

    context = {
        'formset': formset,
        'data': noPel,
    }
    return render(request, 'apps/create_sppt_lama.html', context)
    
@login_required(login_url='login')
@admin_only
def manage_sppt_baru(request, id):
    nospptlama = SPPTLama.objects.get(id=id)
    SpptBaruInlineFormSet = inlineformset_factory(SPPTLama, SPPTBaru, form=SPPTBaruForm, extra=0)
    formset = SpptBaruInlineFormSet(instance=nospptlama)
    if request.method == "POST":
        formset = SpptBaruInlineFormSet(request.POST, instance=nospptlama)
        if formset.is_valid():
            formset.save()
            print('success')
            # Do something. Should generally end with a redirect. For example:
            return redirect('/pendataan')
        else:
            print('ERROR', formset.errors)
    else:
        formset = SpptBaruInlineFormSet(instance=nospptlama)

    context = {
        'formset': formset,
        'spptlama':nospptlama,
    }
    return render(request, 'apps/create_sppt_baru.html', context)

