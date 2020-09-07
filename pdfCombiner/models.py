from django.db import models


# Create your models here.
class Pdf(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    pdf_file_name = models.CharField(max_length=40, unique=True)
    pdf_file = models.FileField(upload_to='pdf/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_pdf_path(instance, pdf_file):
        return '/pdf/' + pdf_file


