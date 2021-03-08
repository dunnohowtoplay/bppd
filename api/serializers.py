from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.models import Pendaftaran, Desa, Kecamatan

class PendaftaranSerializer(serializers.ModelSerializer):
    #desa= serializers.ReadOnlyField(source='desa.nama')
    #kecamatan= serializers.ReadOnlyField(source='kecamatan.nama')
    class Meta:
        model = Pendaftaran
        extra_kwargs = {'no_pelayanan': {'read_only': True}}
        fields= (
            'tanggal_pendaftaran',
            'no_pelayanan',
            'nama',
            'desa',
            'kecamatan',
            'mutasi',
            'jumlah',
            'keterangan',
            'tanggal_selesai',
            'kontak',
            )
