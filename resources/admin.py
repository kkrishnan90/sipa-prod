from django.contrib import admin

from resources.models import Resources

# Register your models here.
@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display=['title','description','created_on']