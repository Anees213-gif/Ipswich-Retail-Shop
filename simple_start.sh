#!/bin/bash

echo "🚀 Starting simple Django deployment..."

# Navigate to backend directory
cd backend

echo "📁 Current directory: $(pwd)"
echo "📋 Python version: $(python --version)"
echo "📋 Django version: $(python -c 'import django; print(django.get_version())')"

echo "🔄 Testing Django configuration..."
python manage.py check --deploy

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
echo "🚀 Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:$PORT --timeout 120 --workers 1 --access-logfile - --error-logfile - ipswich_retail.wsgi:application
