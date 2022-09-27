from django.shortcuts import render
from resources.models import Resources
from home.models import Footer
from contact.models import Contact
# Create your views here.
def getResourcesPage(request):
      footer_content = Footer.objects.first()
      contact = Contact.objects.latest('created_on')
      resources = Resources.objects.first()
      return render(request,'resources.html',{'footer':footer_content,'resource':resources,'contact':contact,})