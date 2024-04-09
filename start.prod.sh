#!/bin/bash
source .venv/Scripts/activate
cd /code || exit
mkdir staticfiles || echo "staticfiles folder already existed"
echo "-----------Apply migration--------- "
python manage.py makemigrations
python manage.py migrate
echo "-----------Collect static files-----------"
python manage.py collectstatic --noinput

echo "-----------Run gunicorn--------- "
gunicorn logNewAlbum.wsgi:application --bind 0.0.0.0:8000
