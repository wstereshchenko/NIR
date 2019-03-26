from celery import shared_task


@shared_task
def aaa():
    print('ok')
