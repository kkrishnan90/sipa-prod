from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from order_confirmation.views import  getOrderConfirmation
from orders.views import orderSuccess
app_name = 'order_confirmation'
urlpatterns = [
    path('/',view=getOrderConfirmation,name='order_confirmation'),
    path('/success',view=orderSuccess,name='success'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
