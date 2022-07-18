from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"portfolio/index.html")

def contact_us(request):
    if request.method == "POST":
        message_name=request.POST['name']
        message_email=request.POST['email']
        message=request.POST['message']

        # send an email
        try:
            send_mail(
                message_name, #subject
                message, # message
                message_email, # from email
                ['vikramkumar8655@gmail.com'], # to email
                )
        except:
            return render(request, 'portfolio/index.html',{
            'resp': 2
            })
        return render(request, 'portfolio/index.html',{
            'resp': 3
        })
    else:
        return render(request, 'portfolio/index.html')