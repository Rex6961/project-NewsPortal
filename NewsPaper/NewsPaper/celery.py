import os
import time
from celery.schedules import crontab
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_every_monday_at_8am': {
        'task': 'news.tasks.send_week_news_posts',
        'schedule': crontab(minute='00', hour='08', day_of_week='monday'),
    },
}
