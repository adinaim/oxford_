from django.contrib import admin

from .models import (
    EngSchoolPage, 
    EngSchoolImages,
    EngSchoolInfo,
    EngSchoolInfoImages
)

admin.site.register([EngSchoolPage, EngSchoolImages, EngSchoolInfo, EngSchoolInfoImages])