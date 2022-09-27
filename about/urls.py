from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from about.views import getAboutPageDetails

app_name = 'about'
urlpatterns = [
    path('/',view=getAboutPageDetails,name='about')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
