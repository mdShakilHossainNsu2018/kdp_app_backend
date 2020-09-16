from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from .models import Pdf


class PdfSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='pdf-detail', lookup_field='id')
    pdf_file = serializers.FileField(required=False, max_length=None, use_url=True, allow_empty_file=True,
                                     allow_null=True)
    class Meta:
        model = Pdf
        fields = ['id', 'url', 'pdf_file', 'pdf_file_name', 'total_pages',  'created_at', 'updated_at']
        read_only_fields = ['id']
