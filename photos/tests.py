from django.test import TestCase
from .models import Photo

# Create your tests here.

class PhotoModelTest(TestCase):
    def test_create_photo(self):
        """Test creating a photo object"""
        photo = Photo.objects.create(
            title="Test Photo",
            description="Test Description",
            s3_key="photos/test.jpg",
            s3_url="http://localhost:4566/photo-bucket/photos/test.jpg"
        )
        self.assertEqual(photo.title, "Test Photo")
        self.assertEqual(photo.description, "Test Description")
        self.assertIsNotNone(photo.uploaded_at)
        self.assertIsNotNone(photo.updated_at)

    def test_photo_str(self):
        """Test the string representation of photo"""
        photo = Photo.objects.create(
            title="My Photo",
            description="",
            s3_key="photos/my.jpg",
            s3_url="http://localhost:4566/photo-bucket/photos/my.jpg"
        )
        self.assertEqual(str(photo), "My Photo")

    def test_photo_ordering(self):
        """Test that photos are ordered by uploaded_at descending"""
        photo1 = Photo.objects.create(
            title="First",
            s3_key="photos/first.jpg",
            s3_url="http://localhost:4566/photo-bucket/photos/first.jpg"
        )
        photo2 = Photo.objects.create(
            title="Second",
            s3_key="photos/second.jpg",
            s3_url="http://localhost:4566/photo-bucket/photos/second.jpg"
        )
        photos = Photo.objects.all()
        self.assertEqual(photos[0].title, "Second")
        self.assertEqual(photos[1].title, "First")

