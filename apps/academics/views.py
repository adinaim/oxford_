from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


from apps.news.permissions import IsOwner
from .models import (
    AcademicsPage,
    AcademicsInfo
)
from .serializers import (
    AcademicsCreateSerializer,
    AcademicsListSerializer,
    AcademicsPageSerializer,
    AcademicsInfoCreateSerializer,
    AcademicsInfoListSerializer,
    AcademicsInfoSerializer,
)


class AcademicsPageViewSet(ModelViewSet):
    queryset = AcademicsPage.objects.all()
    serializer_class = AcademicsPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AcademicsListSerializer
        elif self.action == 'create':
            return AcademicsCreateSerializer
        elif self.action == 'retrieve':
            return AcademicsPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class AcademicsInfoViewSet(ModelViewSet):
    queryset = AcademicsInfo.objects.all()
    serializer_class = AcademicsInfoSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AcademicsInfoListSerializer
        elif self.action == 'create':
            return AcademicsInfoCreateSerializer
        elif self.action == 'retrieve':
            return AcademicsInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()