from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    return render(request, 'leadtech/index.html')

@api_view(['POST'])
def contact_api(request):
    message_name=request.POST['name']
    message_email=request.POST['email']
    message_subject=request.POST['subject']
    message=request.POST['message']
    if (message_email=="")or(message_name==""):
        return JsonResponse({'message':"Please fill all details..",'success':False})
    if ("@" not in message_email):
        return JsonResponse({'message':"Invalid email, Please check..",'success':False})

    # send an email
    send_mail(
        (message_name+": "+message_subject), #subject
        ("(FROM: "+message_email+") \n"+message), # message
        message_email, # from email
        ['vikramkumar8655@gmail.com'], # to email
        )
    send_mail("Vikram Kumar", f"Thank You {message_name}, I will contact you as soon as Possible..",'vikramkumar8655@gmail.com',[message_email],True)
    return JsonResponse({'message':"Thank You! Your form has been successfully submited..",
        'success':True
    })