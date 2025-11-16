from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import boto3
from django.conf import settings
import uuid
from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_s3_client(self):
        """Get S3 client configured for LocalStack"""
        return boto3.client(
            's3',
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
            use_ssl=settings.AWS_S3_USE_SSL,
            verify=settings.AWS_S3_VERIFY
        )

    def create(self, request, *args, **kwargs):
        """Upload photo to S3 and create database record"""
        file = request.FILES.get('file')
        title = request.data.get('title', '')
        description = request.data.get('description', '')

        if not file:
            return Response(
                {'error': 'No file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Generate unique filename
            file_extension = file.name.split('.')[-1]
            s3_key = f"photos/{uuid.uuid4()}.{file_extension}"

            # Upload to S3
            s3_client = self.get_s3_client()
            s3_client.upload_fileobj(
                file,
                settings.AWS_STORAGE_BUCKET_NAME,
                s3_key,
                ExtraArgs={'ContentType': file.content_type}
            )

            # Generate S3 URL
            s3_url = f"{settings.AWS_S3_ENDPOINT_URL}/{settings.AWS_STORAGE_BUCKET_NAME}/{s3_key}"

            # Create database record
            photo = Photo.objects.create(
                title=title or file.name,
                description=description,
                s3_key=s3_key,
                s3_url=s3_url
            )

            serializer = self.get_serializer(photo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, *args, **kwargs):
        """Delete photo from S3 and database"""
        instance = self.get_object()

        try:
            # Delete from S3
            s3_client = self.get_s3_client()
            s3_client.delete_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=instance.s3_key
            )

            # Delete from database
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

