#!/bin/bash
source .venv/Scripts/activate
cd /code || exit
echo "-----------Apply migration--------- "
python manage.py makemigrations
python manage.py migrate

