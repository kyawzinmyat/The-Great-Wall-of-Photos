# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-upload-url/', views.get_presigned_url, name='get-upload-url'),
    path('photos/', views.list_photos, name='list-photos')
]