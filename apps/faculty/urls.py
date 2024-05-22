from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    DepartmentViewSet,
    FacultyViewSet,
)


router = DefaultRouter()
router.register('department', DepartmentViewSet)
router.register('faculty', FacultyViewSet)


urlpatterns = [ 
]

urlpatterns += router.urls