from django.shortcuts import render,redirect
from .models import users
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['name']
        password = request.POST['password']
        try:
            user = users.objects.get(email=email)
            if check_password(password,user.password):
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Invalid Password'})
        except users.DoesNotExist:
            return render(request,'login.html',{'error': 'Email does not exist'})
    else:
        return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        user = users(name=name,email=email,password=hashed_password)
        user.save()
        return redirect('login')
    else:
        return render(request,'signup.html')
def home_view(request):
    return render(request,'home.html')
    