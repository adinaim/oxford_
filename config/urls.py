from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Oxford API",
      default_version='v1',
      description="This is oxford school api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('admin/', admin.site.urls),

   path('api/academics/', include('apps.academics.urls')),
   path('api/account/', include('apps.account.urls')),
   path('api/admissions/', include('apps.admissions.urls')),
   path('api/engschool/', include('apps.engschool.urls')),
   path('api/faculty/', include('apps.faculty.urls')),
   path('api/information/', include('apps.information.urls')),
   path('api/kindergarten/', include('apps.kindergarten.urls')),
   path('api/news/', include('apps.news.urls')),
   path('api/questions/', include('apps.questions.urls')),
   path('api/ruschool/', include('apps.ruschool.urls')),
]