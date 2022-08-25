from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@api_view(['GET'])
def index(request):
    return render(request, 'leadtech/layout.html')