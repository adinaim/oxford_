from django.db import models
from slugify import slugify


class Department(models.Model):
    slug = models.SlugField(max_length=40, blank=True, primary_key=True)
    title = models.CharField(max_length=15)
    about = models.CharField(max_length=400)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    head = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class DepartmentImage(models.Model):
    image = models.ImageField(upload_to='media/department_images')
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        related_name='department_images'
    )


class Faculty(models.Model):
    POSITION_CHOICES = (           # change
        ('var1', 'Var 1'),
        ('var2', 'Var 2'),
        ('var3', 'Var 3')
    )
    
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    joined = models.DateField()
    email = models.EmailField()
    about = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/faculty_staff')
    department = models.ForeignKey(
        to=Department,
        on_delete=models.DO_NOTHING,
        related_name='department_faculty'
    )
    position = models.CharField(choices=POSITION_CHOICES, max_length=5)
    slug = models.SlugField(max_length=40, blank=True, primary_key=True)


    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name) + '-' + slugify(self.last_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Faculty and staff'
        verbose_name_plural = 'Faculty and staff'