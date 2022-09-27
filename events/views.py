from django.shortcuts import render

from home.models import Footer
from events.models import Events
from contact.models import Contact
# Create your views here.

def getEventDetailPage(request):
    contact = Contact.objects.latest('created_on')
    footer_content = Footer.objects.first()
    events = Events.objects.order_by('date').all()       
    return render(request, 'events.html',{'footer':footer_content,'events':events,'contact':contact,})