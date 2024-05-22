from django.db import models

from slugify import slugify

from apps.faculty.models import Faculty


class AboutUsPage(models.Model):
    slug = models.SlugField(max_length=25, blank=True, primary_key=True)
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'About us page'
        verbose_name_plural = 'Pages'


class AboutUsPageImage(models.Model):
    image = models.ImageField(upload_to='media/about_us_page_images')
    page = models.ForeignKey(
        to=AboutUsPage,
        on_delete=models.CASCADE,
        related_name='about_us_images',
    )


class AboutUsInfo(models.Model):
    slug = models.SlugField(max_length=25, blank=True, primary_key=True)
    page = models.ForeignKey(
        to=AboutUsPage,
        on_delete=models.DO_NOTHING,
        related_name='abou_us_info'
    )
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'About us info'
        verbose_name_plural = 'Info'


class AboutUsInfoImage(models.Model):
    image = models.ImageField(upload_to='media/about_us_info_images')
    info = models.ForeignKey(
        to=AboutUsInfo,
        on_delete=models.CASCADE,
        related_name='about_us_info_images',
    )


class Information(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=20)
    principal = models.ForeignKey(
        to=Faculty,
        on_delete=models.DO_NOTHING
    )
    logo = models.ImageField(upload_to='media/logo')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Information'