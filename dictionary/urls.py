from django.urls import path
from .views import hello_world

urlpatterns = [
    path('dictionary/', hello_world)
    # path('upload-pdf/', PdfListCreateApiView.as_view()),
    # path('download-pdf/', PdfDownloadAndDeleteView.as_view()),
]
