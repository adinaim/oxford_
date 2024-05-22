from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    FAQViewSet,
    ContactUsViewSet,
)


router = DefaultRouter()
router.register('faq', FAQViewSet)
router.register('contact-us', ContactUsViewSet)


urlpatterns = [ 
]

urlpatterns += router.urls