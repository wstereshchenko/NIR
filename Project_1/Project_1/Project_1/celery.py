import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')

app = Celery('Project_1')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.enable_utc = False

CELERY_BEAT_SCHEDULE = {
    'owm': {
        'task': 'owm.tasks.owm_save_to_base',
        'schedule': crontab(minute='*'),
    },
}
