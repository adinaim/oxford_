from django.db import models
from slugify import slugify


class EngSchoolPage(models.Model):
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
        verbose_name = 'English School page'
        verbose_name_plural = 'English School pages'


class EngSchoolImages(models.Model):
    image = models.ImageField(upload_to='media/engschool_image')
    page = models.ForeignKey(
        to=EngSchoolPage,
        on_delete=models.CASCADE,
        related_name='engschool_page_images',
    )


class EngSchoolInfo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    page = models.ForeignKey(
        to=EngSchoolPage,
        on_delete=models.CASCADE,
        related_name='engschool_info',
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
        verbose_name = 'English School info'
        verbose_name_plural = 'English School info'


class EngSchoolInfoImages(models.Model):
    image = models.ImageField(upload_to='media/engschool_image')
    info = models.ForeignKey(
        to=EngSchoolInfo,
        on_delete=models.CASCADE,
        related_name='engschool_info_images',
    )