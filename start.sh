#!/bin/bash
echo "Running Migrations..."
python manage.py migrate

echo "Collecting Static Files..."
python manage.py collectstatic --noinput

echo "Starting Server..."
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
