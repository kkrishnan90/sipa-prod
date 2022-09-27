from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from resources.views import  getResourcesPage
app_name = 'resources'
urlpatterns = [
    path('/',view=getResourcesPage,name='resources'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)