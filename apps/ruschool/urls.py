from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    RuSchoolPageViewSet,
    RuSchoolInfoViewSet,
)


router = DefaultRouter()
router.register('page', RuSchoolPageViewSet, 'ruschool')
router.register('info', RuSchoolInfoViewSet, 'ruschool_info')


urlpatterns = [ 
]

urlpatterns += router.urls