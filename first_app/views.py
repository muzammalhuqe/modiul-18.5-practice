from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_singup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = RegistrationForm()
        return render(request, 'user_singup.html', {'form' : form})
    else:
        return redirect('profile')

    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']
                user = authenticate(username = name, password = userpassword)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'user_login.html', {'form' : form})
    else:
        return redirect('profile')


def user_profile(request):
    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'pass_change.html', {'form' : form})
    else:
        return redirect('login')
    

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'pass_change2.html', {'form' : form})
    else:
        return redirect('login')
    
