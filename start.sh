#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Ipswich Retail Shop deployment..."

# Navigate to backend directory
cd backend

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
gunicorn --bind 0.0.0.0:$PORT ipswich_retail.wsgi:application
