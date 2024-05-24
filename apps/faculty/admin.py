from django.contrib import admin

from .models import (
    Department,
    DepartmentImage,
    Faculty
)

admin.site.register([Department, DepartmentImage, Faculty])