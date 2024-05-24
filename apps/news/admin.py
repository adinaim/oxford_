from django.contrib import admin

from .models import (
    News, 
    NewsImage,
    Tag,
    Event,
    EventImage
)

admin.site.register([News, NewsImage, Tag, Event, EventImage])