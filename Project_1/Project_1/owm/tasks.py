from celery import shared_task


@shared_task
def aaa():
    return 1
