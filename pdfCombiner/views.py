from rest_framework import generics, viewsets
from .models import Pdf
from .serializers import PdfSerializer
from PyPDF2 import PdfFileReader


class PdfModelViewSet(viewsets.ModelViewSet):
    serializer_class = PdfSerializer
    # parser_classes = (FileUploadParser,)
    queryset = Pdf.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        total_pages = PdfFileReader(self.request.data.get('pdf_file')).getNumPages()
        serializer.save(ip=ip, total_pages=total_pages)











