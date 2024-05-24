from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)


from .models import (
    RuSchoolPage,
    RuSchoolInfo
)
from .serializers import (
    RuSchoolCreateSerializer,
    RuSchoolListSerializer,
    RuSchoolPageSerializer,
    RuSchoolInfoCreateSerializer,
    RuSchoolInfoListSerializer,
    RuSchoolInfoSerializer,
)


class RuSchoolPageViewSet(ModelViewSet):
    queryset = RuSchoolPage.objects.all()
    serializer_class = RuSchoolPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return RuSchoolListSerializer
        elif self.action == 'create':
            return RuSchoolCreateSerializer
        elif self.action == 'retrieve':
            return RuSchoolPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class RuSchoolInfoViewSet(ModelViewSet):
    queryset = RuSchoolInfo.objects.all()
    serializer_class = RuSchoolInfoSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return RuSchoolInfoListSerializer
        elif self.action == 'create':
            return RuSchoolInfoCreateSerializer
        elif self.action == 'retrieve':
            return RuSchoolInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()