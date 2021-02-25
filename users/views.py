from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')

    else:
        form = CreateUserForm()
        
    context = {
        'form':form,
    }

    return render(request, 'users/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('success')
            return redirect('apps:home')
        else:
            print('failed')
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('apps:home')


