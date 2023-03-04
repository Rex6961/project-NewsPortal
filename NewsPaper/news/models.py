from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache
from django.utils.translation import gettext as _

# Create your models here.

class Author(models.Model):
    authUser = models.OneToOneField(User, on_delete=models.CASCADE, help_text=_('Author'))
    
    rateAuthor = models.SmallIntegerField(default=0, help_text=_('Rate'))

    def update_rating(self):
        post_rate = self.post_set.aggregate(postRating=Sum('rate_news'))
        pRat = 0
        pRat += post_rate.get('postRating')

        comment_rate = self.authUser.comment_set.aggregate(commentRating=Sum('rate_comment'))
        cRat = 0
        cRat += comment_rate.get('commentRating')

        self.rateAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.authUser}'



class Category(models.Model):
    category = models.CharField(max_length=64, unique=True, help_text=_('Category'))
    subscribers = models.ManyToManyField(User, related_name='categories', help_text=_('Subscribers'))

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text=_('Author'))
    category = models.ManyToManyField(Category, through='PostCategory', help_text=_('Category'))
    
    NEWS = 'NE'
    ARTICLE = 'AR'

    CATEGORY_CHOICES = (
        (NEWS, _('Новости')),
        (ARTICLE, _('Статья'))
    )
    change_news = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, help_text=_('change news'))
    time_in = models.DateTimeField(auto_now_add=True, help_text=_('time in'))
    head_news = models.CharField(max_length=128, help_text=_('head news'))
    text_news = models.TextField(help_text=_('text news'))
    rate_news = models.SmallIntegerField(default=0, help_text=_('rate news'))

    def __str__(self):
        return f'{self.head_news}'

    def like(self):
        self.rate_news += 1
        self.save()

    def dislike(self):
        self.rate_news -= 1
        self.save()

    def preview(self):
        return f'{self.text_news[:50]}...'

    def get_absolute_url(self):
        return reverse('new', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')





class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, help_text=_('post'))
    authUser = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('authorization users'))

    text_comment = models.TextField(default='без комментариев', help_text=_('comments'))
    time_in = models.DateTimeField(auto_now_add=True, help_text=_('time in'))
    rate_comment = models.SmallIntegerField(default=0, help_text=_('rate comment'))

    def like(self):
        self.rate_comment += 1
        self.save()

    def dislike(self):
        self.rate_comment -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, help_text=_('post'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text=_('category'))

    def __str__(self):
        return f'{self.post.head_news} {self.category}'
