from django.db import models

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