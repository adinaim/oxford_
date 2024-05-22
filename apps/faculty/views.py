from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)


from apps.news.permissions import IsOwner
from .models import (
    Department,
    Faculty
)
from .serializers import (
    DepartmentCreateSerializer,
    DepartmentListSerializer,
    DepartmentRetrieveSerializer,
    DepartmentListSerializer,
    FacultySerializer,
    FacultyListSerializer
)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentCreateSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update', 'update']:
            return DepartmentCreateSerializer
        elif self.action == 'list':
            return DepartmentListSerializer
        elif self.action == 'retrieve':
            return DepartmentRetrieveSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def get_serializer_class(self):
        if self.action in ['create', 'retrieve', 'partial_update', 'update']:
            return FacultySerializer
        elif self.action == 'list':
            return FacultyListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()