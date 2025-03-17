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



def booking(request):
    if request.method == "POST":
        mybookings = Booking(
            name=request.POST['name'],
            email=request.POST['email'],
            phonenumber=request.POST['phone'],
            datetime=request.POST['date'],

            message=request.POST['message']
        )
        mybookings.save()
        return redirect('/show')
    else:
        return render(request, 'contact.html')


def contacts(request):
    if request.method == "POST":
        mybooking= Booking(
        name= request.POST['name'],
        email =request.POST['email'],
        phonenumber = request.POST['phone'],
        datetime = request.POST['date'],
        message = request.POST['message']
        )
        mybooking.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def show(request):
    all = Booking.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
  deletebooking=Booking.objects.get(id=id)
  deletebooking.delete()
  return redirect('/show')

def edit(request,id):
    booking=get_object_or_404(Booking,id=id)
    if request.method == "POST":
        Booking.name=request.POST.get('name')
        Booking.email=request.POST.get('email')
        Booking.phonenumber=request.POST.get('phonenumber')
        Booking.datetime=request.POST.get('datetime')
        Booking.message=request.POST.get('message')
        Booking.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html',{'Booking':booking})
