from django.shortcuts import render
from .models import *
# Create your views here.
app_name = 'apps'
def index(request):
    desas = Desa.objects.all()
    kecamatans = Kecamatan.objects.all()
    datas = Pendaftaran.objects.all()
    context = {
        'datas':datas,
        'desas':desas,
        'kecamatans':kecamatans,
        }
    return render(request, 'apps/index.html', context)