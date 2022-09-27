from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods

from contact.models import Contact
from events.models import Events
from home.models import Announcement, Footer, Gallery, LatestNews, Members, Slider, WelcomeNote
from sponsorship.models import Sponsorship

@require_http_methods(["GET"])    
def hello(request):    
    return HttpResponse('<h1>This is Http GET request.</h1>')  

def getHomePageDetails(request):
    contact = Contact.objects.latest('id')
    sliders = Slider.objects.order_by('created_on').all()
    events = Events.objects.order_by('date').all()       
    mission_note = WelcomeNote.objects.order_by('created_on').first()
    photos = Gallery.objects.all()
    news_list = LatestNews.objects.all()
    announcement = Announcement.objects.latest('id')
    events_count = Events.objects.all().count()
    photos_count = Gallery.objects.all().count()
    members_count = Members.objects.all().count()
    sponsorships = Sponsorship.objects.all()
    footer_content = Footer.objects.first()
    return render(request, 'index.html', {'contact':contact,'sliders':sliders,'events':events,
    'mission':mission_note,'events_count':events_count,'photos_count':photos_count,'members_count':members_count,
    'photos':photos, 'news_list':news_list,'announcement':announcement,'footer':footer_content,
    'sponsorships':sponsorships,
    })

def getLatestNews(request):
    contact = Contact.objects.latest('id')
    footer_content = Footer.objects.first()
    news_list = LatestNews.objects.all()
    return render(request, 'news.html', {'contact':contact,'news_list':news_list,'footer':footer_content,
    })