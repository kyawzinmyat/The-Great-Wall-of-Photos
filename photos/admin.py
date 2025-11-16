from django.contrib import admin
from .models import Photo

# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 's3_key']
    list_filter = ['uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'updated_at']

