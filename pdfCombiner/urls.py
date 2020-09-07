from .views import PdfModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()

router.register('pdf', PdfModelViewSet)

urlpatterns = [
    path('pdf/', include(router.urls))
    # path('upload-pdf/', PdfListCreateApiView.as_view()),
    # path('download-pdf/', PdfDownloadAndDeleteView.as_view()),
]