from django.shortcuts import render
from puja2022.models import Puja
from home.models import Footer
from contact.models import Contact
# Create your views here.
def getPujaContentPage(request):
      contact = Contact.objects.latest('created_on')
      footer_content = Footer.objects.first()
      puja = Puja.objects.first()
      return render(request,'puja2022.html',{'footer':footer_content,'puja':puja,'contact':contact})