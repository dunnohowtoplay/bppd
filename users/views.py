from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
# Create your views here.

from .forms import CreateUserForm
from .decorators import unauthenticated_user

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)

            messages.success(request, 'Account was created for '+ username)
            
            return redirect('login')

    else:
        form = CreateUserForm()
        
    context = {
        'form':form,
    }

    return render(request, 'users/register.html', context)

@unauthenticated_user
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


