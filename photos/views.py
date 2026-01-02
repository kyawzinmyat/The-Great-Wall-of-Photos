# views.py
import boto3
from django.conf import settings
from django.http import JsonResponse
from botocore.config import Config
import os
from dotenv import load_dotenv
import uuid
from .models import Photo


def list_photos(request):
    # 1. Get all photo records from the DB
    photos = Photo.objects.all().order_by('-uploaded_at')
    
    # 2. Setup S3 Client (Same as before)
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        config=Config(signature_version='s3v4', s3={'addressing_style': 'path'})
    )

    gallery_data = []

    for photo in photos:
        # 3. Generate a temporary "View" URL for each photo
        # This math happens locally on your CPU (it's fast), no network call needed.
        try:
            presigned_url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Key': photo.s3_key
                },
                ExpiresIn=3600 # Link works for 1 hour
            )
            
            gallery_data.append({
                'id': photo.id,
                'title': photo.title,
                'description': photo.description,
                'image_url': presigned_url,
                'uploaded_at': photo.uploaded_at.isoformat(),
                'updated_at': photo.updated_at.isoformat()
            })
        except Exception as e:
            print(f"Error signing url for {photo.s3_key}: {e}")

    return JsonResponse({'photos': gallery_data})


def get_presigned_url(request):
    # Setup the S3 client using settings
    # Load environment variables from .env file
    load_dotenv()
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        config=Config(signature_version='s3v4')
    )

    # Get the filename they intend to upload (sent from React)
    file_name = request.GET.get('file_name')
    if not file_name:
        return JsonResponse({'error': 'File name required'}, status=400)

    file_extension = file_name.split('.')[-1]
    s3_key = f"photos/{uuid.uuid4()}.{file_extension}"
    try:
        # Generate the URL
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': s3_key,
                'ContentType': 'image/jpeg' # Or make this dynamic based on file type
            },
            ExpiresIn=3600
        )
        Photo.objects.create(
            title=request.GET.get('title', 'Untitled'),
            description=request.GET.get('description', ''),
            s3_key=s3_key,
            s3_url=presigned_url
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'url': presigned_url})