# Generated by Django 4.1.5 on 2023-02-20 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='change_news_en_us',
        ),
        migrations.RemoveField(
            model_name='post',
            name='change_news_es_ar',
        ),
        migrations.RemoveField(
            model_name='post',
            name='change_news_ru_ru',
        ),
    ]
