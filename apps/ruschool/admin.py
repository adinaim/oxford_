from django.contrib import admin

from .models import (
    RuSchoolPage, 
    RuSchoolImages,
    RuSchoolInfo,
    RuSchoolInfoImages
)

admin.site.register([RuSchoolPage, RuSchoolImages, RuSchoolInfo, RuSchoolInfoImages])