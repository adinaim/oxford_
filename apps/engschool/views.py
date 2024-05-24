from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)


from .models import (
    EngSchoolPage,
    EngSchoolInfo
)
from .serializers import (
    EngSchoolCreateSerializer,
    EngSchoolListSerializer,
    EngSchoolPageSerializer,
    EngSchoolInfoCreateSerializer,
    EngSchoolInfoListSerializer,
    EngSchoolInfoSerializer,
)


class EngSchoolPageViewSet(ModelViewSet):
    queryset = EngSchoolPage.objects.all()
    serializer_class = EngSchoolPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return EngSchoolListSerializer
        elif self.action == 'create':
            return EngSchoolCreateSerializer
        elif self.action == 'retrieve':
            return EngSchoolPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class EngSchoolInfoViewSet(ModelViewSet):
    queryset = EngSchoolInfo.objects.all()
    serializer_class = EngSchoolInfoSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return EngSchoolInfoListSerializer
        elif self.action == 'create':
            return EngSchoolInfoCreateSerializer
        elif self.action == 'retrieve':
            return EngSchoolInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()