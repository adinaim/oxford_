from django.db import models
from slugify import slugify


class RuSchoolPage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Russian School page'
        verbose_name_plural = 'Russian School pages'


class RuSchoolImages(models.Model):
    image = models.ImageField(upload_to='media/ruschool_image')
    page = models.ForeignKey(
        to=RuSchoolPage,
        on_delete=models.CASCADE,
        related_name='ruschool_page_images',
    )


class RuSchoolInfo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    page = models.ForeignKey(
        to=RuSchoolPage,
        on_delete=models.CASCADE,
        related_name='ruschool_info',
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
        verbose_name = 'Russian School info'
        verbose_name_plural = 'Russian School info'


class RuSchoolInfoImages(models.Model):
    image = models.ImageField(upload_to='media/ruschool_image')
    info = models.ForeignKey(
        to=RuSchoolInfo,
        on_delete=models.CASCADE,
        related_name='ruschool_info_images',
    )