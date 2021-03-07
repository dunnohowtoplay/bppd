from django.db import models
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
    kontak = models.CharField(max_length=15, blank=True,  null=True)

    def __str__(self):
        return f"{self.no_pelayanan} - {self.nama}"

class SPPTLama(models.Model):
    no_pelayanan = models.ForeignKey(Pendaftaran,  null=True, blank=True, on_delete=models.CASCADE)
    no_sppt_lama = models.CharField(max_length=18, blank=True,  null=True)
    nama_wp_lama = models.CharField(max_length=100)
    tarif_lama = models.DecimalField(max_digits=19, decimal_places=4, blank=True)
    luas_tanah_lama = models.IntegerField(blank=True, null=True)
    luas_bangunan_lama = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.no_pelayanan.nama} - {self.nama_wp_lama}"


class SPPTBaru(models.Model):
    KET_TRANSAKSI = [
    ('Tetap', 'Tetap'),
    ('Baru', 'Baru'),
    ('Naik', 'Naik'),
    ('Turun', 'Turun'),
    ]
    TRANSAKSI = [
    ('Jual Beli', 'Jual Beli'),
    ('Hibah', 'Hibah'),
    ('Waris', 'Waris'),
    ('Penghapusan', 'Penghapusan'),
    ('AJB', 'AJB'),
    ('Sertifikat', 'Sertifikat'),
    ('Dll', 'Dll'),
    ]
    sppt_lama = models.ForeignKey(SPPTLama,  null=True, blank=True, on_delete=models.CASCADE)
    no_sppt_baru = models.CharField(max_length=18, blank=True,  null=True)
    nama_wp_baru = models.CharField(max_length=100)
    tarif_baru = models.DecimalField(max_digits=19, decimal_places=4, blank=True)
    keterangan = models.CharField(max_length=20, choices=KET_TRANSAKSI, blank=True)
    transaksi = models.CharField(max_length=20, choices=TRANSAKSI, blank=True)
    luas_tanah_baru = models.IntegerField(blank=True, null=True)
    luas_bangunan_baru = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.sppt_lama.no_pelayanan.no_pelayanan} - {self.sppt_lama.no_pelayanan.nama} - {self.sppt_lama.nama_wp_lama} - {self.nama_wp_baru}"
#class Pendataan(models.Model):




