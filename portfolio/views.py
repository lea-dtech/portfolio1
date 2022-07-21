from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"portfolio/index.html")

def contact_api(request):
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
        send_mail("Vikram Kumar", f"Thank You {message_name}, I will contact you as soon as Possible..",'vikramkumar8655@gmail.com',[message_email],True)
        return render(request, 'portfolio/index.html',{
            'resp': True
        })
    else:
        return HttpResponseRedirect(reverse('portfolio:index'))