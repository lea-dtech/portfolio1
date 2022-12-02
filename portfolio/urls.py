from django.urls import path

from . import views

app_name="portfolio"
urlpatterns=[
    path("",views.index,name='index'),
    path("contact_api",views.contact_api,name='contact_api'),
    path("contact_private",views.contact_private,name='contact_private'),
]

