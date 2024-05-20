from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AcademicsPageViewSet,
    AcademicsInfoViewSet,
)


router = DefaultRouter()
router.register('page', AcademicsPageViewSet, 'academics')
router.register('info', AcademicsInfoViewSet, 'academics_info')


urlpatterns = [ 
]

urlpatterns += router.urls