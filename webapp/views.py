from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def homepage(request):
    return render(request,'home.html')

def contactpage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        # send an email
        send_mail(
            'message from' + name,# subject
            message,# message
            email,# from email
           ['trailerworld1309@gmail.com'], # to email

        )


        return render(request,'contact.html',{'user':name})



    else:
     return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def pricing(request):
    return render(request,'pricing.html')


def services(request):
    return render(request,'services.html')


def portofolio(request):
    return render(request,'portofolio.html')