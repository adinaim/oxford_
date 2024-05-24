from django.db import models
from slugify import slugify


class KindergartenPage(models.Model):
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
        verbose_name = 'Kindergaten page'
        verbose_name_plural = 'Kindergaten pages'


class KindergartenImages(models.Model):
    image = models.ImageField(upload_to='media/kindergarten_image')
    page = models.ForeignKey(
        to=KindergartenPage,
        on_delete=models.CASCADE,
        related_name='kindergarten_page_images',
    )


class KindergartenInfo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    page = models.ForeignKey(
        to=KindergartenPage,
        on_delete=models.CASCADE,
        related_name='kindergarten_info',
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
        verbose_name = 'Kindergarten info'
        verbose_name_plural = 'Kindergarten info'


class KindergartenInfoImages(models.Model):
    image = models.ImageField(upload_to='media/kindergarten_image')
    info = models.ForeignKey(
        to=KindergartenInfo,
        on_delete=models.CASCADE,
        related_name='kindergarten_info_images',
    )