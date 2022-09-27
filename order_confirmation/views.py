from django.shortcuts import render
from contact.models import Contact
# Create your views here.
from home.models import  Footer

def getOrderConfirmation(request):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    return render(request, 'order-confirmation.html',{'footer':footer_content,'contact':contact,})
