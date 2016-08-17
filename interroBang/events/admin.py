from django.contrib import admin

# Register your models here.
from .models import Event

class EventModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Event

admin.site.register(Event, EventModelAdmin)