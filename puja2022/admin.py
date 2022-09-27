from django.contrib import admin

from puja2022.models import Puja

# Register your models here.
@admin.register(Puja)
class PujaAdmin(admin.ModelAdmin):
    list_display=['title','content','created_on']