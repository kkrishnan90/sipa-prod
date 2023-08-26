"""sipa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('admin/', admin.site.urls),
    path(r'',include('home.urls'),name='home'),
    path(r'home',include('home.urls',namespace='home')),
    path(r'about',include('about.urls',namespace='about')),
    path(r'gallery',include('gallery.urls',namespace='gallery')),
    path(r'events',include('events.urls',namespace='events')),
    path(r'sponsorship',include('sponsorship.urls',namespace='sponsorship')),
    path(r'resources',include('resources.urls',namespace='resources')),
    path(r'puja2022',include('puja2022.urls',namespace='puja2022')),
    path(r'orders',include('orders.urls',namespace='orders')),
    path(r'orders-confirmation',include('order_confirmation.urls',namespace='order_confirmation')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
