from django.db import models
import os, uuid


# id = uuid.uuid1()
from django.db.models.signals import pre_save
from django.dispatch import receiver


def pdf_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    # chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    # randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'pdf/{randomstring}{ext}'.format(randomstring=uuid.uuid4(), ext=file_extension)


# Create your models here.
class Pdf(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    pdf_file_name = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to=pdf_path, blank=True, null=True)
    total_pages = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_pdf_path(instance, pdf_file):
        return '/pdf/' + pdf_file


@receiver(pre_save, sender=Pdf)
def my_callback(sender, instance, *args, **kwargs):
    file = instance.pdf_file_name
    if(len(instance.pdf_file_name)>20):
        file = instance.pdf_file_name[:12] + '...' + instance.pdf_file_name[-5:]
    instance.pdf_file_name = file
