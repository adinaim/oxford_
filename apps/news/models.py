from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model

from datetime import datetime


User = get_user_model()

class News(models.Model):

    STATUS_CHOICES = (
        ('important', 'Important'),
        ('unimportant', 'Unimportant')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='news',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(
        to='Tag',
        related_name='news_tags'
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug =  str(slugify(self.title))[:4] + str(datetime.now())[19:23] 
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class NewsImage(models.Model):
    image = models.ImageField(upload_to='media/news_image')
    news = models.ForeignKey(
        to=News,
        on_delete=models.CASCADE,
        related_name='news_images',
    )


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    slug = models.SlugField(max_length=28, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.tag

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug =  str(slugify(self.tag))
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class Events(models.Model):
    TYPE_CHOICES = (
        ('out', 'Outside of school'),
        ('at', 'At school'),
        ('parents', 'For parents'),
    )

    slug = models.SlugField(max_length=25, blank=True, primary_key=-True)
    title = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug =  str(slugify(self.title)) + slugify(self.date)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class EventImage(models.Model):
    ...