from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth,logout
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.

def signup (request):
    if request.method == "POST":
       data = request.POST
       text = data.get('text')
       email = data.get('email')
       password = data.get('password')
       password2 = data.get('password2')
       my_user = User.objects.create_user(username=text,email=email,password=password)
       my_user.save()
       return redirect('/loginn/')
       
    return render(request,"login.html")

def login (request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('logpassword')
        user = authenticate(request,username=username, email = email, password=password)
        
        if user is None:
            return redirect('/loginn/')
        else:
             auth(request,user)
             return redirect('/mypatient/')
        
    return render(request, 'loginn.html')

def mypatient (request):
    return render(request,'mypatient.html')

def ambulance (request):
    return render(request,'ambulance.html')

def health (request):
    return render(request,'health.html')

def order (request):
    return render(request,'order.html')

def about (request):
    return render(request,'about.html')

def logoutpage(request):
    logout(request)
    return redirect('/loginn/')

def loginpage():
    return redirect('/loginn/')