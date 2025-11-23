from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_time', 'end_time', 'is_passed')
    list_filter = ('start_time', 'is_active')
    search_fields = ('title', 'description')
