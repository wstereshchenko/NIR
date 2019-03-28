import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')

app = Celery('Project_1')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
