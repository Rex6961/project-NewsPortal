from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import PostCategory
from .tasks import send_email_notifications_new_articles


def send_notifications(preview, pk, head_news, subscribers):
    send_email_notifications_new_articles.delay(
        preview, pk, head_news, subscribers
    )


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails: list[str] = []

        for category in categories:
            subscribers = category.subscribers.all()

            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.head_news, subscribers_emails)
