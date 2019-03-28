#!/usr/bin/env bash
python wait_for_db.py

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000