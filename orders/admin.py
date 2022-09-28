from django.contrib import admin

from orders.models import OrderModel

# Register your models here.
@admin.register(OrderModel)
class EventsAdmin(admin.ModelAdmin):
    list_display=['csrf_token','name','email','event_name','event_date','qr_code_img_url','family_count','prasad_count','created_on']