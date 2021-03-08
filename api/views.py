from rest_framework import generics
from apps.models import Pendaftaran
from api.serializers import PendaftaranSerializer
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

@receiver(pre_save, sender=Pendaftaran)
@receiver(post_save, sender=Pendaftaran)
class SnippetList(generics.ListCreateAPIView):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer

@receiver(pre_save, sender=Pendaftaran)
@receiver(post_save, sender=Pendaftaran)
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer
