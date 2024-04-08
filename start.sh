#!/bin/bash
source .venv/Scripts/activate
cd /code || exit
echo "-----------Apply migration--------- "
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:5000

