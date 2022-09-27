from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from events.views import getEventDetailPage

app_name = 'events'
urlpatterns = [
    path('/',view=getEventDetailPage,name='events')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
