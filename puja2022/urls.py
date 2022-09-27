from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from puja2022.views import  getPujaContentPage
app_name = 'puja2022'
urlpatterns = [
    path('/',view=getPujaContentPage,name='puja2022'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)