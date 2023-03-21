from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def index(request):
    # ip=get_ip(request)
    # u=User(user=ip)
    # result=User.objects.filter(Q(user__icontains=ip))
    # if len(result)>=1:
    #     pass
    # else:
    #     u.save()
    # count=User.objects.all().count()
    data={
        'visitor_count':12,
    }
    return render(request,"portfolio/index.html",data)

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

def contact_private(request):
    return render(request,"portfolio/personal.html")

def get_ip(request):
    address=request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip=address.split(',')[-1].strip()
    else:
        ip=request.META.get('REMOTE_ADDR')
    return ip
