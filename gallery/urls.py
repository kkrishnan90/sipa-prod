from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from gallery.views import  getGalleryPageDetails
app_name = 'gallery'
urlpatterns = [
    path('/',view=getGalleryPageDetails,name='gallery'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
