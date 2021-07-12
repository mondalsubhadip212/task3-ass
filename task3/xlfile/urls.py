from django.urls import path

from . import views

urlpatterns = [
    path('file_upload',views.FileUpload.as_view())
]