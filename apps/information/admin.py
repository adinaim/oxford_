from django.contrib import admin

from .models import (
    AboutUsPage, 
    AboutUsPageImage,
    AboutUsInfo,
    AboutUsInfoImage,
    Information
)

admin.site.register([AboutUsPage, AboutUsPageImage, AboutUsInfo, AboutUsInfoImage, Information])