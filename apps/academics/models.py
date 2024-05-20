from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class AcademicsPage(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='academics',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Academics'
        verbose_name_plural = 'Academics'


class AcademicsImages(models.Model):
    image = models.ImageField(upload_to='media/academics_image')
    page = models.ForeignKey(
        to=AcademicsPage,
        on_delete=models.CASCADE,
        related_name='academics_images',
    )


class AcademicsInfo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='academics_info_user',
    )
    page = models.ForeignKey(
        to=AcademicsPage,
        on_delete=models.CASCADE,
        related_name='academics_info',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Academics'
        verbose_name_plural = 'Academics'


class AcademicsInfoImages(models.Model):
    image = models.ImageField(upload_to='media/academics_image')
    info = models.ForeignKey(
        to=AcademicsInfo,
        on_delete=models.CASCADE,
        related_name='academics_info_images',
    )
