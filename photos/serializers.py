from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'description', 's3_key', 's3_url', 'uploaded_at', 'updated_at']
        read_only_fields = ['id', 's3_key', 's3_url', 'uploaded_at', 'updated_at']
