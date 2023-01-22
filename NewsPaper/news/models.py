from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache

# Create your models here.

class Author(models.Model):
    authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    
    rateAuthor = models.SmallIntegerField(default=0)

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
    category = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.category}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    NEWS = 'NE'
    ARTICLE = 'AR'

    CATEGORY_CHOICES = (
        (NEWS, 'Новости'),
        (ARTICLE, 'Статья')
    )
    change_news = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    time_in = models.DateTimeField(auto_now_add=True)
    head_news = models.CharField(max_length=128)
    text_news = models.TextField()
    rate_news = models.SmallIntegerField(default=0)

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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    authUser = models.ForeignKey(User, on_delete=models.CASCADE)

    text_comment = models.TextField(default='без комментариев')
    time_in = models.DateTimeField(auto_now_add=True)
    rate_comment = models.SmallIntegerField(default=0)

    def like(self):
        self.rate_comment += 1
        self.save()

    def dislike(self):
        self.rate_comment -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.head_news} {self.category}'
