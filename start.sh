#!/bin/bash

# The Great Wall of Photos - Startup Script

echo "🏯 Starting The Great Wall of Photos..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start LocalStack
echo "📦 Starting LocalStack..."
docker-compose up -d

# Wait for LocalStack to be ready
echo "⏳ Waiting for LocalStack to be ready..."
sleep 5

# Check if LocalStack is ready
until docker-compose exec -T localstack awslocal s3 ls > /dev/null 2>&1; do
    echo "⏳ Still waiting for LocalStack..."
    sleep 2
done

echo "✅ LocalStack is ready!"

# Apply Django migrations
echo "🔧 Running Django migrations..."
python manage.py migrate

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Start Django backend: python manage.py runserver"
echo "   2. In a new terminal, start React frontend: npm start"
echo "   3. Open http://localhost:3000 in your browser"
echo ""
echo "💡 Tip: Make sure both servers are running to use the application"
echo ""
