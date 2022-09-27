from django.shortcuts import render
from home.models import Footer
from sponsorship.models import SponsorNote, Sponsorship
from contact.models import Contact
# Create your views here.
def getSponsorshipDetailsPage(request):
    sponsorships = Sponsorship.objects.all()
    contact = Contact.objects.latest('created_on')
    footer_content = Footer.objects.first()
    sponsornote = SponsorNote.objects.latest('created_on')
    return render(request,'sponsorships.html',{'footer':footer_content,'sponsorships':sponsorships,
    'sponsornote':sponsornote,'contact':contact})