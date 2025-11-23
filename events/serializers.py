from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  'description',
                  'start_time',
                  'end_time',
                  'user',
                  'is_active',
                  'is_passed'
                  )
        read_only_fields = ('user', 'is_passed')
