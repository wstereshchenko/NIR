import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
app = Celery('Project_1')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULER = {
    'owm': {
        'task': 'owm.tasks.owm_save_to_base',
        'schedule': crontab(minute='*'),
    },
}
