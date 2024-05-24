from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)


from .models import (
    KindergartenPage,
    KindergartenInfo
)
from .serializers import (
    KindergartenCreateSerializer,
    KindergartenListSerializer,
    KindergartenPageSerializer,
    KindergartenInfoCreateSerializer,
    KindergartenInfoListSerializer,
    KindergartenInfoSerializer,
)


class KindergartenPageViewSet(ModelViewSet):
    queryset = KindergartenPage.objects.all()
    serializer_class = KindergartenPageSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return KindergartenListSerializer
        elif self.action == 'create':
            return KindergartenCreateSerializer
        elif self.action == 'retrieve':
            return KindergartenPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class KindergartenInfoViewSet(ModelViewSet):
    queryset = KindergartenInfo.objects.all()
    serializer_class = KindergartenInfoSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return KindergartenInfoListSerializer
        elif self.action == 'create':
            return KindergartenInfoCreateSerializer
        elif self.action == 'retrieve':
            return KindergartenInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()