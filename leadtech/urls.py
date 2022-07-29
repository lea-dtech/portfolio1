from django.urls import path

from . import views

app_name="leadtech"
urlpatterns=[
    path("",views.index,name='index'),
]

