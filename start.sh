#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Ipswich Retail Shop deployment..."

# Navigate to backend directory
cd backend

echo "📁 Current directory: $(pwd)"
echo "📋 Files in current directory:"
ls -la

echo "🔄 Running database migrations..."
python manage.py migrate

echo "🔄 Collecting static files..."
python manage.py collectstatic --noinput

echo "🔄 Loading sample data..."
python manage.py load_sample_data

# Start the server
echo "🚀 Starting Django server..."
if [ -z "$PORT" ]; then
    PORT=8000
fi

echo "🌐 Starting server on port $PORT"
echo "🔍 Testing Django setup..."
python manage.py check

echo "🚀 Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:$PORT --timeout 120 --workers 2 --access-logfile - --error-logfile - ipswich_retail.wsgi:application
