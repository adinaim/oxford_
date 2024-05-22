from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


from apps.news.permissions import IsOwner
from .models import (
    FAQ,
    ContactUs,
)
from .serializers import (
    FAQSerializer,
    ContactUsSerializer
)


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def get_permissions(self):
        if self.action in ['create',]:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'list', 'retrieve', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()