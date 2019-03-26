#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
celery -A worker -l info