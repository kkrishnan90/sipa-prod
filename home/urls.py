from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from home.views import  getHomePageDetails,getLatestNews
app_name = 'home'
urlpatterns = [
    path('',view=getHomePageDetails,name='home'),
    path('/',view=getHomePageDetails,name='home'),
    path('/latest-news',view=getLatestNews,name='latest-news'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
