from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    KindergartenPageViewSet,
    KindergartenInfoViewSet,
)


router = DefaultRouter()
router.register('page', KindergartenPageViewSet, 'kindergarten')
router.register('info', KindergartenInfoViewSet, 'kindergarten_info')


urlpatterns = [ 
]

urlpatterns += router.urls