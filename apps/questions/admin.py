from django.contrib import admin

from .models import (
    FAQ,
    ContactUs
)

admin.site.register([FAQ, ContactUs])