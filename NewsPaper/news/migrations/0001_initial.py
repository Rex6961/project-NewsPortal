# Generated by Django 4.1.5 on 2023-02-20 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rateAuthor', models.SmallIntegerField(default=0, help_text='Rate')),
                ('authUser', models.OneToOneField(help_text='Author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(help_text='Category', max_length=64, unique=True)),
                ('subscribers', models.ManyToManyField(help_text='Subscribers', related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_news', models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статья')], default='AR', help_text='change news', max_length=2)),
                ('change_news_en_us', models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статья')], default='AR', help_text='change news', max_length=2, null=True)),
                ('change_news_es_ar', models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статья')], default='AR', help_text='change news', max_length=2, null=True)),
                ('change_news_ru_ru', models.CharField(choices=[('NE', 'Новости'), ('AR', 'Статья')], default='AR', help_text='change news', max_length=2, null=True)),
                ('time_in', models.DateTimeField(auto_now_add=True, help_text='time in')),
                ('head_news', models.CharField(help_text='head news', max_length=128)),
                ('head_news_en_us', models.CharField(help_text='head news', max_length=128, null=True)),
                ('head_news_es_ar', models.CharField(help_text='head news', max_length=128, null=True)),
                ('head_news_ru_ru', models.CharField(help_text='head news', max_length=128, null=True)),
                ('text_news', models.TextField(help_text='text news')),
                ('text_news_en_us', models.TextField(help_text='text news', null=True)),
                ('text_news_es_ar', models.TextField(help_text='text news', null=True)),
                ('text_news_ru_ru', models.TextField(help_text='text news', null=True)),
                ('rate_news', models.SmallIntegerField(default=0, help_text='rate news')),
                ('author', models.ForeignKey(help_text='Author', on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(help_text='category', on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('post', models.ForeignKey(help_text='post', on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(help_text='Category', through='news.PostCategory', to='news.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField(default='без комментариев', help_text='comments')),
                ('time_in', models.DateTimeField(auto_now_add=True, help_text='time in')),
                ('rate_comment', models.SmallIntegerField(default=0, help_text='rate comment')),
                ('authUser', models.ForeignKey(help_text='authorization users', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(help_text='post', on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
    ]
