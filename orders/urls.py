from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


<<<<<<< HEAD
from orders.views import   orderSuccess, renderOrderForm,exportcsv, addVisitConfirmation
=======
from orders.views import   orderSuccess, renderOrderForm, addVisitConfirmation
>>>>>>> ece432e038afc9466938c992c094e58f0b78e574
app_name = 'orders'
urlpatterns = [
    path(r'/^$',view=renderOrderForm,name='orders'),
    path(r'/success/<csrf_token>',view=orderSuccess,name='success'),
    path(r'/confirmation/<csrf_token>',view=addVisitConfirmation,name='confirmation'),
<<<<<<< HEAD
    path(r'/export',view=exportcsv,name='exportcsv'),
=======
>>>>>>> ece432e038afc9466938c992c094e58f0b78e574
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
