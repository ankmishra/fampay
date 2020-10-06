from celery import shared_task

@shared_task
def fetch_latest_videos(x, y):
    return x + y