# Quick Start Guide

## Prerequisites
- Python 3.8+ installed
- Node.js 14+ installed  
- Docker and Docker Compose installed

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Copy environment file:**
   ```bash
   cp .env.example .env
   ```

## Running the Application

### Option 1: Using the startup script (Linux/Mac)
```bash
./start.sh
```
Then in separate terminals:
```bash
# Terminal 1
python manage.py runserver

# Terminal 2  
npm start
```

### Option 2: Manual startup

1. **Start LocalStack:**
   ```bash
   docker-compose up -d
   ```

2. **Run Django migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Start Django backend:**
   ```bash
   python manage.py runserver
   ```

4. **Start React frontend (in a new terminal):**
   ```bash
   npm start
   ```

5. **Access the application:**
   Open http://localhost:3000 in your browser

## Stopping the Application

1. Stop the Django server: Press `Ctrl+C` in the Django terminal
2. Stop the React server: Press `Ctrl+C` in the React terminal
3. Stop LocalStack:
   ```bash
   docker-compose down
   ```

## Testing LocalStack

Verify S3 bucket creation:
```bash
# Install awscli-local if needed
pip install awscli-local

# List S3 buckets
awslocal s3 ls
```

You should see `photo-bucket` listed.

## Common Issues

**Issue:** Can't connect to LocalStack
- **Solution:** Make sure Docker is running: `docker ps`
- Check if LocalStack is running: `docker-compose ps`

**Issue:** CORS errors in browser
- **Solution:** Make sure both Django (port 8000) and React (port 3000) are running

**Issue:** Photos not uploading
- **Solution:** Check that LocalStack is running and the S3 bucket exists
- Verify with: `awslocal s3 ls`

## Features

- ✅ Upload photos with title and description
- ✅ View photos in a responsive grid gallery
- ✅ Delete photos from gallery
- ✅ Photos stored in LocalStack S3
- ✅ Metadata stored in SQLite database

## API Endpoints

- `GET /api/photos/` - List all photos
- `POST /api/photos/` - Upload new photo
- `GET /api/photos/{id}/` - Get specific photo
- `DELETE /api/photos/{id}/` - Delete photo

## Tech Stack

- **Frontend:** React 18
- **Backend:** Django 5.0 + Django REST Framework
- **Storage:** LocalStack (AWS S3 simulation)
- **Database:** SQLite
- **File Upload:** boto3

Enjoy using The Great Wall of Photos! 🏯📸
