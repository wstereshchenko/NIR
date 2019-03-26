import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')

app = Celery('Project_1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
