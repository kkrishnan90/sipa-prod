from django.shortcuts import render,redirect
from contact.models import Contact
from home.models import  Footer
from django.contrib import messages

from orders.models import NonMemberModel, OrderModel
from django.core.files import File
import urllib

# Create your views here.
from .forms import  OrderNonMemberForm
from django.conf import settings
import time
import qrcode
from django.contrib.staticfiles.storage import staticfiles_storage

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from home.models import  Footer

def renderOrderForm(request):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    form = OrderNonMemberForm(request.POST)
    event_date = request.GET['event_date']
    
    if request.method == 'POST':
        print('Request coming from SUBMIT POST')        
        form = OrderNonMemberForm(request.POST) 
        # print(form.errors)
        if form.is_valid():                    
            result = generateQRAndSave(request,form)
            if result:
                return HttpResponseRedirect(reverse('orders:success',kwargs={'csrf_token':form.data.get('csrfmiddlewaretoken')}))             
    else:
        form = OrderNonMemberForm()
    return render(request, 'orders.html',{'form':form,'footer':footer_content,'contact':contact,'event_date':event_date})

def addVisitConfirmation(request,csrf_token=None):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    order = OrderModel.objects.get(csrf_token=csrf_token)
    print(order)
    return render(request, 'scan-success.html',{'footer':footer_content,'contact':contact,'order':order})

def orderSuccess(request,csrf_token=None):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    order = OrderModel.objects.filter(csrf_token=csrf_token).first()
    return render(request, 'order-confirmation.html',{'footer':footer_content,'contact':contact,'order':order})

def generateQRAndSave(request,form):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)   
    constructed_url = "http://{}/orders/confirmation/{}".format(request.get_host(),form.data.get('csrfmiddlewaretoken'))           
    qr.add_data(constructed_url)                  
    qr.make(fit=True)          
    img = qr.make_image(fill_color="black", back_color="white")    
    temp_save_dir = settings.MEDIA_ROOT+'orders/'
    file_name = form.data.get('csrfmiddlewaretoken')+'.png'
    img.save("{}{}".format(temp_save_dir,file_name))            
    image_url = "http://{}{}{}{}".format(request.get_host(),settings.MEDIA_URL,'orders/',file_name)            
    OrderModel.objects.update_or_create(csrf_token = form.data.get('csrfmiddlewaretoken'),name=form.data.get('name'),
    email=form.data.get('email'),event_date=request.GET['event_date'],
    qr_code_img_url=image_url,family_count=form.data.get('family_count'),prasad_count=form.data.get('prasad_count'),phone=form.data.get('phone'))
    return True

def testing(request,id):
    data = id
    return render(request,'testing.html',{'data':data})