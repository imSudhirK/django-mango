from django.shortcuts import render, redirect, HttpResponse 
from datetime import datetime
from mango.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        print("aaksnfdjks")
        return redirect("/login-user")
    context = {
        'var01': 11111,
        'var02': 22222,
    }
    return render(request, 'index.html', context)

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login-user")
    return render(request, 'dashboard.html')

def about(request):
    if request.user.is_anonymous:
        return redirect("/login-user")
    return render(request, 'about.html')

def services(request):
    if request.user.is_anonymous:
        return redirect("/login-user")
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        newContact = Contact(name = name, email = email, description = description, date = datetime.today())
        newContact.save()
        messages.success(request, "Your request has been sent")
    

    return render(request, 'contact.html')

def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username, email, password)
        User.objects.create_user(username, email, password)
        return redirect("/login-user")
    return render(request, "register.html")

def loginUser(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login-user")



