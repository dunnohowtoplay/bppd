from django.db import models
from django.db.models.signals import pre_save,post_save
import datetime

# Create your models here.
class Kecamatan(models.Model):
    nama = models.CharField(max_length=30)

    def __str__(self):
        return self.nama

class Desa(models.Model):
    nama = models.CharField(max_length=30)
    kecamatan = models.ForeignKey(Kecamatan, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Pendaftaran(models.Model):
    KET_CHOICES = [
    ('PROSES', 'PROSES'),
    ('SELESAI', 'SELESAI'),
    ]
    tanggal_pendaftaran = models.DateField()
    no_pelayanan=models.CharField(max_length=11, unique=True, blank=True, null=True, default=0)
    nama = models.CharField(max_length=100)
    desa = models.ForeignKey(Desa,  null=True, blank=True, on_delete=models.DO_NOTHING)
    kecamatan = models.ForeignKey(Kecamatan, null=True, blank=True, on_delete=models.DO_NOTHING)
    mutasi = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    keterangan = models.CharField(max_length=20, choices=KET_CHOICES)
    tanggal_selesai = models.DateField()

    def __str__(self):
        return f"{self.no_pelayanan} - {self.nama}"

class SPPTLama(models.Model):
    no_pelayanan = models.ForeignKey(Pendaftaran,  null=True, blank=True, on_delete=models.DO_NOTHING)
    no_sppt_lama = models.CharField(max_length=18, unique=True, blank=True,  null=True)
    nama_wp_lama = models.CharField(max_length=100)
    tarif_lama = models.DecimalField(max_digits=19, decimal_places=4, blank=True)

    def __str__(self):
        return f"{self.no_pelayanan.nama} - {self.nama_wp_lama}"


class SPPTBaru(models.Model):
    KET_TRANSAKSI = [
    ('TETAP', 'TETAP'),
    ('BARU', 'BARU'),
    ('NAIK', 'NAIK'),
    ('TURUN', 'TURUN'),
    ]
    sppt_lama = models.ForeignKey(SPPTLama,  null=True, blank=True, on_delete=models.DO_NOTHING)
    no_sppt_baru = models.CharField(max_length=18, unique=True, blank=True,  null=True)
    nama_wp_baru = models.CharField(max_length=100)
    tarif_baru = models.DecimalField(max_digits=19, decimal_places=4, blank=True)
    keterangan = models.CharField(max_length=20, choices=KET_TRANSAKSI, blank=True)
    transaksi = models.CharField(max_length=20, blank=True)
    luas_tanah = models.IntegerField(blank=True, null=True)
    luas_bangunan = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.sppt_lama.no_pelayanan.no_pelayanan} - {self.sppt_lama.no_pelayanan.nama} - {self.sppt_lama.nama_wp_lama} - {self.nama_wp_baru}"
#class Pendataan(models.Model):



#Signals configurations
edit = False
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
    global thdint,edit
    if instance.no_pelayanan != "0":
        edit = True
    else:
        edit = False
        if len(Pendaftaran.objects.all()) < 1:
            thdint = 1
            instance.no_pelayanan = f"{datetime.datetime.now().year}{str(secint).zfill(4)}{str(thdint).zfill(3)}"
            print(instance.no_pelayanan)
        else:
            instance.no_pelayanan = f"{datetime.datetime.now().year}{str(secint).zfill(4)}{str(thdint).zfill(3)}"
            print(instance.no_pelayanan)

pre_save.connect(editPK, sender=Pendaftaran)

def postPK(sender, instance, **kwargs):
    global secint,thdint,edit
    if edit == True:
        edit = False
    else:
        if thdint % 200 == 0:
            secint += 1
            thdint = 1
        else:
            thdint += 1
        print(thdint)

post_save.connect(postPK, sender=Pendaftaran)
