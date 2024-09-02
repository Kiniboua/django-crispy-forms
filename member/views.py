from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def register(request):
    if  request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else: 
        form = UserChangeForm()
    return render(request, 'authentication/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('home')

# Create your views here.
