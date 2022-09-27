from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods

from about.models import About, CommitteMembers
from events.models import Events
from home.models import Footer, Gallery, Members
from contact.models import Contact

@require_http_methods(["GET"])    
def hello(request):    
    return HttpResponse('<h1>This is Http GET request.</h1>')  

def getAboutPageDetails(request):
    contact = Contact.objects.latest('created_on')
    abouts = About.objects.all()
    events_count = Events.objects.all().count()
    photos_count = Gallery.objects.all().count()
    members_count = Members.objects.all().count()
    footer_content = Footer.objects.first()
    committee_members = CommitteMembers.objects.all()
    return render(request, 'about.html',{'abouts':abouts,'events_count':events_count,'photos_count':photos_count,
    'members_count':members_count,'footer':footer_content,'committee_members':committee_members,'contact':contact})