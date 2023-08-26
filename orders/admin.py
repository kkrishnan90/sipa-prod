from django.contrib import admin

from orders.models import OrderModel

# Register your models here.
@admin.register(OrderModel)
class EventsAdmin(admin.ModelAdmin):
    list_display=['name','email','event_name','event_date','family_count',
'prasad_count','is_verified','created_on']
