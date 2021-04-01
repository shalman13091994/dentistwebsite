from django.urls import path
from.views import homepage,contactpage,about,portofolio,services,pricing

urlpatterns=[
    path('',homepage,name='home'),
    path('contact.html',contactpage,name='contact'),
    path('about.html',about,name='about'),
    path('portofolio.html',portofolio,name='portofolio'),
    path('services.html',services,name='services'),
    path('pricing.html',pricing,name='pricing'),

]
