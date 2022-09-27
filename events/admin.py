from django.contrib import admin

from events.models import Events

# Register your models here.
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display=['title','description','date','created_on']