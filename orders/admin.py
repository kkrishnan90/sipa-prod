from django.contrib import admin

from orders.models import OrderModel

# Register your models here.
@admin.register(OrderModel)
class EventsAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display=['name','email','event_name','event_date','family_count',
'prasad_count','is_verified','created_on']
=======
    list_display=['csrf_token','name','email','event_name','event_date','qr_code_img_url','family_count','prasad_count','created_on']
>>>>>>> ece432e038afc9466938c992c094e58f0b78e574
