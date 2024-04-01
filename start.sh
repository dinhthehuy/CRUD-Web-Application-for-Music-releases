#!/bin/bash
source .venv/Scripts/activate
cd /code || exit
rm -r staticfiles || echo "found no staticfiles folder"
mkdir staticfiles
echo "-----------Apply migration--------- "
python manage.py makemigrations
python manage.py migrate
echo "-----------Collect static files-----------"
python manage.py collectstatic

echo "-----------Run gunicorn--------- "
gunicorn logNewAlbum.wsgi:application --bind 0.0.0.0:8000
