from django.db import models
from django.db.models.signals import pre_save,post_save
import datetime

# Create your models here.
class Kecamatan(models.Model):
    kecamatan = models.CharField(max_length=30)

    def __str__(self):
        return self.kecamatan

class Desa(models.Model):
    desa = models.CharField(max_length=30)
    kecamatan = models.ForeignKey(Kecamatan, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.desa

class Pendaftaran(models.Model):
    KET_CHOICES = [
    ('PROSES', 'PROSES'),
    ('SELESAI', 'SELESAI'),
    ]
    tanggal_pendaftaran = models.DateField()
    no_pelayanan=models.CharField(max_length=11, unique=True, blank=True, null=True, default=0)
    nama = models.CharField(max_length=100)
    desa = models.ForeignKey(Desa,  null=True, blank=True, on_delete=models.CASCADE)
    kecamatan = models.ForeignKey(Kecamatan, null=True, blank=True, on_delete=models.CASCADE)
    mutasi = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    keterangan = models.CharField(max_length=20, choices=KET_CHOICES)
    tanggal_selesai = models.DateField()

    def __str__(self):
        return f"{self.no_pelayanan} - {self.nama}"


#Signals configurations

if len(Pendaftaran.objects.all()) < 1:
    secint = 1
    thdint = 1
else:
    thdint = int(Pendaftaran.objects.latest('id').no_pelayanan[-3:])+1
    if int(Pendaftaran.objects.latest('id').no_pelayanan[-3:]) == 200:
        secint = int(Pendaftaran.objects.latest('id').no_pelayanan[4:8]) + 1
    else:
        secint = int(Pendaftaran.objects.latest('id').no_pelayanan[4:8])


def editPK(sender, instance, **kwargs):
    global thdint
    if len(Pendaftaran.objects.all()) < 1:
        thdint = 1
        instance.no_pelayanan = f"{datetime.datetime.now().year}{str(secint).zfill(4)}{str(thdint).zfill(3)}"
        print(instance.no_pelayanan)
    else:
        instance.no_pelayanan = f"{datetime.datetime.now().year}{str(secint).zfill(4)}{str(thdint).zfill(3)}"
        print(instance.no_pelayanan)

pre_save.connect(editPK, sender=Pendaftaran)

def postPK(sender, instance, **kwargs):
    global secint,thdint
    if thdint % 200 == 0:
        secint += 1
        thdint = 1
    else:
        thdint += 1
    print(thdint)

post_save.connect(postPK, sender=Pendaftaran)
