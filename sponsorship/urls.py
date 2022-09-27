from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from sponsorship.views import  getSponsorshipDetailsPage
app_name = 'sponsorship'
urlpatterns = [
    path('/',view=getSponsorshipDetailsPage,name='sponsorship'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
