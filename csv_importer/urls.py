from django.urls import path
from .views import CategoryUploadView

urlpatterns = [
    path('importcategory/', CategoryUploadView.as_view(), name='importcategory')
]