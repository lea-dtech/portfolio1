from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"portfolio/index.html")

def contact_us(request):
    if request.method == "POST":
        message_name=request.POST['name']
        message_email=request.POST['email']
        message_subject=request.POST['subject']
        message=request.POST['message']
    
        # send an email
        send_mail(
            (message_name+": "+message_subject), #subject
            ("(FROM: "+message_email+") \n"+message), # message
            message_email, # from email
            ['vikramkumar8655@gmail.com'], # to email
            )
        return render(request, 'portfolio/index.html',{
            'resp': True
        })
    else:
        return render(request, 'portfolio/index.html')