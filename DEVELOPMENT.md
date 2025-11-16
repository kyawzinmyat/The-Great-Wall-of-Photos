# Development Guide

## Project Overview

This is a learning project demonstrating how to build a full-stack application with:
- React (Frontend SPA)
- Django REST Framework (Backend API)
- LocalStack (Local AWS S3 simulation)

## Architecture

```
┌─────────────────┐      HTTP/AJAX      ┌──────────────────┐
│                 │ ──────────────────> │                  │
│  React Frontend │                     │  Django Backend  │
│  (Port 3000)    │ <────────────────── │  (Port 8000)     │
│                 │      JSON API       │                  │
└─────────────────┘                     └──────────────────┘
                                               │
                                               │ boto3
                                               ▼
                                        ┌──────────────────┐
                                        │   LocalStack     │
                                        │   S3 Service     │
                                        │  (Port 4566)     │
                                        └──────────────────┘
```

## Code Structure

### Backend (Django)

**backend/settings.py**
- Django configuration
- CORS settings for React frontend
- AWS/LocalStack S3 configuration
- Installed apps and middleware

**photos/models.py**
- `Photo` model with fields: title, description, s3_key, s3_url, timestamps

**photos/views.py**
- `PhotoViewSet` - API endpoints for CRUD operations
- S3 upload/delete logic using boto3

**photos/serializers.py**
- `PhotoSerializer` - Converts Photo model to/from JSON

**photos/urls.py**
- REST API routing

### Frontend (React)

**src/App.js**
- Main component with upload form and photo gallery
- State management for photos, form data, upload status
- API calls to Django backend using axios

**src/App.css**
- Responsive styling with gradient background
- Grid layout for photo gallery
- Form and button styling

**src/index.js**
- React app entry point

### LocalStack

**docker-compose.yml**
- LocalStack service configuration
- Port mapping (4566 for S3)
- Volume mounting for init scripts

**localstack-init/init-s3.sh**
- Automatically creates `photo-bucket` on startup

## Development Workflow

### Adding a New Feature

1. **Backend (Django)**
   - Update model in `photos/models.py` if needed
   - Run migrations: `python manage.py makemigrations && python manage.py migrate`
   - Update serializer in `photos/serializers.py`
   - Update views in `photos/views.py`
   - Test with: `curl http://localhost:8000/api/photos/`

2. **Frontend (React)**
   - Update component in `src/App.js`
   - Update styles in `src/App.css`
   - Test in browser at `http://localhost:3000`

### Testing S3 Integration

```bash
# List buckets
awslocal s3 ls

# List objects in photo-bucket
awslocal s3 ls s3://photo-bucket/

# Download a photo
awslocal s3 cp s3://photo-bucket/photos/FILENAME.jpg ./test.jpg
```

### Debugging

**Backend Issues:**
```bash
# Check Django logs
python manage.py runserver
# Look for errors in console

# Check database
python manage.py shell
>>> from photos.models import Photo
>>> Photo.objects.all()
```

**Frontend Issues:**
```bash
# Check browser console (F12)
# Look for network errors in Network tab
# Check React component state with React DevTools
```

**LocalStack Issues:**
```bash
# Check LocalStack logs
docker-compose logs -f localstack

# Restart LocalStack
docker-compose restart localstack
```

## API Response Examples

### GET /api/photos/
```json
[
  {
    "id": 1,
    "title": "Sunset",
    "description": "Beautiful sunset photo",
    "s3_key": "photos/uuid.jpg",
    "s3_url": "http://localhost:4566/photo-bucket/photos/uuid.jpg",
    "uploaded_at": "2025-11-16T10:30:00Z",
    "updated_at": "2025-11-16T10:30:00Z"
  }
]
```

### POST /api/photos/
**Request:**
- Content-Type: multipart/form-data
- file: (binary)
- title: "My Photo"
- description: "Description here"

**Response:**
```json
{
  "id": 1,
  "title": "My Photo",
  "description": "Description here",
  "s3_key": "photos/abc-123.jpg",
  "s3_url": "http://localhost:4566/photo-bucket/photos/abc-123.jpg",
  "uploaded_at": "2025-11-16T10:30:00Z",
  "updated_at": "2025-11-16T10:30:00Z"
}
```

## Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True

# AWS/LocalStack
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_STORAGE_BUCKET_NAME=photo-bucket
AWS_S3_ENDPOINT_URL=http://localhost:4566
AWS_S3_REGION_NAME=us-east-1
```

## Best Practices

1. **Never commit `.env` file** - Use `.env.example` as template
2. **Use virtual environment** for Python dependencies
3. **Run migrations** after model changes
4. **Test API endpoints** with curl or Postman before frontend integration
5. **Check browser console** for frontend errors
6. **Use React DevTools** for debugging component state

## Production Considerations

For deploying to production:

1. Use real AWS S3 instead of LocalStack
2. Use PostgreSQL instead of SQLite
3. Set `DEBUG=False` in Django settings
4. Use environment variables for all secrets
5. Serve React build with Django static files or CDN
6. Set up proper CORS policies
7. Use HTTPS for all connections
8. Implement user authentication
9. Add file size and type validation
10. Implement rate limiting

## Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [LocalStack Documentation](https://docs.localstack.cloud/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

Happy coding! 🚀
