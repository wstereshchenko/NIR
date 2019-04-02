import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')
app = Celery('Project_1')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'owm': {
        'task': 'owm.tasks.owm_save_to_base',
        'schedule': crontab(minute=[0, 15, 30, 45])
    },
    'ydx': {
        'task': 'ydx.tasks.ydx_save_to_base',
        'schedule': crontab(minute=[0, 15, 30, 45])
    }
}
