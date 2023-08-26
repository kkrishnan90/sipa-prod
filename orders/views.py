from django.shortcuts import render,redirect
from contact.models import Contact
from home.models import  Footer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from orders.models import NonMemberModel, OrderModel
from django.core.files import File
import urllib
import csv 
from django.http import HttpResponse

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
    event = request.GET['event']
    if request.method == 'POST':
        form = OrderNonMemberForm(request.POST) 
        # print(form.errors)
        if form.is_valid():                    
            result = generateQRAndSave(request,form)
            if result:
                return HttpResponseRedirect(reverse('orders:success',kwargs={'csrf_token':form.data.get('csrfmiddlewaretoken')}))             
    else:
        form = OrderNonMemberForm()
    return render(request, 'orders.html',{'form':form,'footer':footer_content,'contact':contact,'event_date':event_date,'event':event})

def addVisitConfirmation(request,csrf_token=None):
    footer_content = Footer.objects.first()
    contact = Contact.objects.latest('created_on')
    OrderModel.objects.filter(csrf_token=csrf_token).update(is_verified=True)
    order = OrderModel.objects.get(csrf_token=csrf_token)    
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
    email=form.data.get('email'),event_date=request.GET['event_date'],event_name=request.GET['event'],
    qr_code_img_url=image_url,family_count=form.data.get('family_count'),prasad_count=form.data.get('prasad_count'),phone=form.data.get('phone'))
    return True

def exportcsv(request):
    orders = OrderModel.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Event Date', 'Event Name','Phone', 'QR Code','Family Count','Prasad Count','Created On','Is Verified'])
    ords = orders.values_list('name','email', 'event_date', 'event_name','phone', 'qr_code_img_url','family_count','prasad_count','created_on','is_verified')
    for ord in ords:
        writer.writerow(ord)
    return response
