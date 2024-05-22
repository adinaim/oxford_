from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AboutUsPageViewSet,
    AboutUsInfoViewSet,
    InformationViewSet
)


router = DefaultRouter()
router.register('about-us-page', AboutUsPageViewSet)
router.register('about-us-info', AboutUsInfoViewSet)
router.register('information', InformationViewSet)


urlpatterns = [ 
]

urlpatterns += router.urls