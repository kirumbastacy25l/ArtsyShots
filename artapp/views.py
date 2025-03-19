from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from artapp.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')

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




