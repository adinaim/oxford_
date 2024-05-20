from django.contrib import admin

from .models import (
    AdmissionsPage, 
    AdmissionsImages,
    AdmissionsInfo,
    AdmissionsInfoImages
)

admin.site.register([AdmissionsPage, AdmissionsImages, AdmissionsInfo, AdmissionsInfoImages])