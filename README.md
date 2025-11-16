# The Great Wall of Photos

A single-page photo gallery application built with React (frontend) and Django (backend), using LocalStack to simulate AWS S3 for local development.

## 🏗️ Architecture

- **Frontend**: React (Single Page Application)
- **Backend**: Django + Django REST Framework
- **Storage**: AWS S3 (LocalStack for local development)
- **Database**: SQLite (development)

## 🚀 Features

- Upload photos to S3 (LocalStack)
- Display photos in a responsive gallery
- Add titles and descriptions to photos
- Delete photos from both S3 and database
- Modern, gradient UI design

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- Docker and Docker Compose (for LocalStack)

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kyawzinmyat/The-Great-Wall-of-Photos.git
cd The-Great-Wall-of-Photos
```

### 2. Set Up Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

### 3. Start LocalStack

Start LocalStack using Docker Compose:

```bash
docker-compose up -d
```

This will start LocalStack on port 4566 and automatically create the S3 bucket.

### 4. Set Up Django Backend

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 5. Set Up React Frontend

Install Node dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## 🎯 Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Click "Choose Image" to select a photo from your computer
3. Optionally add a title and description
4. Click "Upload Photo" to upload to LocalStack S3
5. View your photos in the gallery below
6. Click "Delete" on any photo to remove it

## 🔧 API Endpoints

- `GET /api/photos/` - List all photos
- `POST /api/photos/` - Upload a new photo
- `GET /api/photos/{id}/` - Get a specific photo
- `PUT /api/photos/{id}/` - Update a photo
- `DELETE /api/photos/{id}/` - Delete a photo

## 🧪 Testing LocalStack

To verify LocalStack is working:

```bash
# Install AWS CLI
pip install awscli-local

# List S3 buckets
awslocal s3 ls

# You should see: photo-bucket
```

## 📁 Project Structure

```
The-Great-Wall-of-Photos/
├── backend/              # Django settings
├── photos/               # Django app for photo management
│   ├── models.py        # Photo model
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   └── urls.py          # API routes
├── public/              # React public files
├── src/                 # React source code
│   ├── App.js          # Main React component
│   ├── App.css         # Styles
│   └── index.js        # React entry point
├── localstack-init/     # LocalStack initialization scripts
├── docker-compose.yml   # LocalStack configuration
├── requirements.txt     # Python dependencies
├── package.json         # Node dependencies
└── README.md           # This file
```

## 🐛 Troubleshooting

### Backend can't connect to LocalStack

Make sure LocalStack is running:
```bash
docker-compose ps
```

### Frontend can't connect to backend

Make sure the Django server is running on port 8000:
```bash
python manage.py runserver
```

### CORS errors

The backend is configured to allow requests from `http://localhost:3000`. If you're using a different port, update `CORS_ALLOWED_ORIGINS` in `backend/settings.py`.

## 📝 Development Notes

- This is a practice project using LocalStack to simulate AWS services
- SQLite is used for simplicity; use PostgreSQL for production
- Photos are stored in LocalStack S3, not on the filesystem
- CORS is enabled for local development

## 🔒 Security Notes

- The current SECRET_KEY is for development only
- Never commit `.env` files with real AWS credentials
- Use environment variables for production settings

## 📄 License

MIT License - feel free to use this project for learning and practice!

