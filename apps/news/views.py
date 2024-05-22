from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)

from .models import (
    News,
    Event
    )
from .serializers import (
    NewsCreateSerializer,
    NewsListSerializer,
    NewsSerializer,
    EventCreateSerializer,
    EventSerializer
)


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return NewsListSerializer
        elif self.action == 'create':
            return NewsCreateSerializer
        elif self.action == 'retrieve':
            return NewsSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'partial_update', 'update']:
            return EventSerializer
        elif self.action == 'create':
            return EventCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()