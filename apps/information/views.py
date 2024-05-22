from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)


from apps.news.permissions import IsOwner
from .models import (
    AboutUsPage,
    AboutUsInfo,
    Information
)
from .serializers import (
    AboutUsCreateSerializer,
    AboutUsListSerializer,
    AboutUsPageSerializer,
    AboutUsInfoCreateSerializer,
    AboutUsInfoListSerializer,
    AboutUsInfoSerializer,
    InformationSerializer
)


class AboutUsPageViewSet(ModelViewSet):
    queryset = AboutUsPage.objects.all()
    serializer_class = AboutUsPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AboutUsListSerializer
        elif self.action == 'create':
            return AboutUsCreateSerializer
        elif self.action == 'retrieve':
            return AboutUsPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class AboutUsInfoViewSet(ModelViewSet):
    queryset = AboutUsInfo.objects.all()
    serializer_class = AboutUsInfoSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AboutUsInfoListSerializer
        elif self.action == 'create':
            return AboutUsInfoCreateSerializer
        elif self.action == 'retrieve':
            return AboutUsInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()