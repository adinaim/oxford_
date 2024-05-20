from django.contrib import admin

from .models import (
    AcademicsPage, 
    AcademicsImages,
    AcademicsInfo,
    AcademicsInfoImages
)

admin.site.register([AcademicsPage, AcademicsImages, AcademicsInfo, AcademicsInfoImages])