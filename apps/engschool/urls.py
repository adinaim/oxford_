from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    EngSchoolPageViewSet,
    EngSchoolInfoViewSet,
)


router = DefaultRouter()
router.register('page', EngSchoolPageViewSet, 'engschool')
router.register('info', EngSchoolInfoViewSet, 'engschool_info')


urlpatterns = [ 
]

urlpatterns += router.urls