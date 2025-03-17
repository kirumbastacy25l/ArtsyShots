from django.shortcuts import render, redirect

from artapp.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'services.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def single(request):
    return render(request, 'gallery-single.html')



def hire(request):
    if request.method == "POST":
        myhirings = hiring(
            name=request.POST['name'],
            email=request.POST['email'],
            phonenumber=request.POST['phone'],
            datetime=request.POST['date'],

            message=request.POST['message']
        )
        myhirings.save()
        return redirect('/show')
    else:
        return render(request, 'hiring.html')


def contacts(request):
    if request.method == "POST":
        mycontacts= Contact(
        name= request.POST['name'],
        email =request.POST['email'],
        phonenumber = request.POST['phone'],
        datetime = request.POST['date'],
        message = request.POST['message']
        )
        mycontacts.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def show(request):
    all = hiring.objects.all()
    return render(request,'show.html',{'all':all})



