from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
from dal import autocomplete
from django.views.generic import View, ListView


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

class Home(View):
    template_name = 'apps/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
'''
def pendaftaran(request):
    datas= Pendaftaran.objects.all()
    desas = Desa.objects.all()
    kecamatans = Kecamatan.objects.all()
    form = PendaftaranForm()
    #formedit = EditPendaftaranForm()
    context = {
        'desas':desas,
        'kecamatans':kecamatans,
        'datas':datas,
        'form':form,
        #'formedit':formedit,
        }
    return render(request, 'apps/pendaftaran.html', context)


def tambahpendaftaran(request):
    form = PendaftaranForm()
    if request.method == "POST":
        form = PendaftaranForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('apps:pendaftaran')

def deletependaftaran(request, *args, **kwargs):
    data_ids=request.POST.getlist('deleteid[]')
    print(data_ids)
    if request.method == "POST":
        for id in data_ids:
            x = Pendaftaran.objects.get(pk=id)
            print(x)
            x.delete()
        
        return redirect('apps:delete-pendaftaran')


'''
class PendaftaranView(View):
    template_name = 'apps/pendaftaran.html'
    '''
    def tambahpendaftaran(self, request, *args, **kwargs):
        if request.method == "POST":
            tambahform = PendaftaranForm(request.POST)
            data_ids=request.POST.getlist('deleteid[]')
            if tambahform.is_valid():
                tambahform.save()

            for id in data_ids:
                x = Pendaftaran.objects.get(pk=id)
                print(x)
                x.delete()
            
            return redirect('apps:pendaftaran')
    '''
    def editpendaftaran(self, request, *args, **kwargs):
        if request.method == "POST":
            editdataid = request.POST.get('editid')
            editdata = get_object_or_404(Pendaftaran, id = editdataid)
            print(editdata)
            editform = PendaftaranForm(request.POST or None, instance=editdata)
            if editform.is_valid():
                    editform.save()

            return redirect('apps:pendaftaran')

    def get(self, request, *args, **kwargs):
        datas= Pendaftaran.objects.all()
        desas = Desa.objects.all()
        kecamatans = Kecamatan.objects.all()
        form = PendaftaranForm()
        #formedit = EditPendaftaranForm()
        context = {
            'desas':desas,
            'kecamatans':kecamatans,
            'datas':datas,
            'form':form,
            #'formedit':formedit,
            }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        datas=Pendaftaran.objects.all()
        desas = Desa.objects.all()
        kecamatans = Kecamatan.objects.all()
        if request.method == "POST":
            tambahform = PendaftaranForm(request.POST)
            data_ids=request.POST.getlist('deleteid[]')
            if tambahform.is_valid():
                tambahform.save()

            for id in data_ids:
                x = Pendaftaran.objects.get(pk=id)
                print(x)
                x.delete()
            
            return redirect('apps:pendaftaran')
        context = {
            'datas':datas,
            'desas':desas,
            'kecamatans':kecamatans,
            'datas':datas,
            }

        return render(request, self.template_name, context)
'''
class TambahPendaftaran(View):
    def  get(self, request):
        tanggal_pendaftaran1 = request.GET.get('tanggal_pendaftaran', None)
        namaWP1 = request.GET.get('namaWP', None)
        kecamatan1 = request.GET.get('kecamatan', None)
        desa1 = request.GET.get('desa', None)
        mutasi1 = request.GET.get('mutasi', None)
        jumlah1 = request.GET.get('jumlah', None)
        keterangan1 = request.GET.get('keterangan', None)
        tanggal_selesai1 = request.GET.get('tanggal_selesai', None)

        obj = Pendaftaran.objects.create(
            tanggal_pendaftaran = tanggal_pendaftaran1,
            nama = namaWP1,
            desa = desa1,
            kecamatan = kecamatan1,
            mutasi = mutasi1,
            jumlah = jumlah1,
            keterangan = keterangan1,
            tanggal_selesai = tanggal_selesai1,
        )

        datadaftar = {'id':obj.id,'tanggal_pendaftaran':obj.tanggal_pendaftaran,'nama':obj.nama,'desa':obj.desa,'kecamatan':obj.kecamatan,'mutasi':obj.mutasi,'jumlah':obj.jumlah,'keterangan':obj.keterangan,'tanggal_selesai':obj.tanggal_selesai}

        data = {
            'datadaftar': datadaftar
        }
        return JsonResponse(data)

class EditPendaftaran(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Pendaftaran.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
'''