

# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from .models import Supply
# from .models import Supplier
# from .forms import SupplyForm
# from .forms import SupplierForm
# import json
from django.shortcuts import render
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# # Create your views here.


def home(request):
    return render(request, 'home.html')
  
  
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'register.html')



def login_view(request):
    
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid input')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')