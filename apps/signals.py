from django.db.models.signals import pre_save,post_save
from .models import *

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
    if instance.no_pelayanan != "":
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