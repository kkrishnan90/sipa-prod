from django.shortcuts import render
from contact.models import Contact
# Create your views here.
from home.models import  Gallery,Footer

def getGalleryPageDetails(request):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    photos = Gallery.objects.all()
    return render(request, 'gallery.html',{'footer':footer_content,'photos':photos,'contact':contact,})