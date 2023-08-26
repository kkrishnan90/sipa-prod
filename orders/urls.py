from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from orders.views import orderSuccess, renderOrderForm, exportcsv, addVisitConfirmation
app_name = 'orders'
urlpatterns = [
    path(r'/^$', view=renderOrderForm, name='orders'),
    path(r'/success/<csrf_token>', view=orderSuccess, name='success'),
    path(r'/confirmation/<csrf_token>',
         view=addVisitConfirmation, name='confirmation'),
    path(r'/export', view=exportcsv, name='exportcsv'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
