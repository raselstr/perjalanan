#!/bin/sh
set -e

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
