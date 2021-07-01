from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:index')

        else :
            messages.error(request, 'Invalid Credentials...')
            return redirect('accounts:login')

    else:
        return render(request, 'account/login.html') 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Email Already Exists...')
                return redirect('accounts:register')
            elif User.objects.filter(username = username).exists():
                messages.error(request, 'Username Already Exists...')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email)
                user.save()
                print('user created ',user.id)
                return redirect('main:index')
            
        else :
            messages.error(request, 'Password Not Matching....')
            return redirect('accounts:register')

    else:
        return render(request, 'account/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('main:index')