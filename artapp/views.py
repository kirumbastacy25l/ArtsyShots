from django.shortcuts import render, redirect, get_object_or_404

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

def delete(request,id):
  deletehiring=hiring.objects.get(id=id)
  deletehiring.delete()
  return redirect('/show')

def edit(request, id, ):
    appointment=get_object_or_404(hiring,id=id)
    if request.method == "POST":
        hiring.name=request.POST.get('name')
        hiring.email=request.POST.get('email')
        hiring.phonenumber=request.POST.get('phonenumber')
        hiring.datetime=request.POST.get('datetime')
        hiring.message=request.POST.get('message')
        hiring.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html',{'hiring':hiring})




