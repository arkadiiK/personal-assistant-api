from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    filterset_fields = ['start_time', 'end_time', 'is_active']
    search_fields = ['title', 'description']
    ordering_fields = ['start_time', 'end_time']
