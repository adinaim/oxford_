from django.contrib import admin

from .models import (
    KindergartenPage, 
    KindergartenImages,
    KindergartenInfo,
    KindergartenInfoImages
)

admin.site.register([KindergartenPage, KindergartenImages, KindergartenInfo, KindergartenInfoImages])