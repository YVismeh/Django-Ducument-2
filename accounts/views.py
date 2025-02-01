from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = request.POST.get('username').strip()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('root:home')
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(request.path_info)
     
    else:
        return render(request, 'registration/login.html')

def logout_user(request):
    return render(request, 'registration/signup.html')
def signup_user(request):
    return render(request, 'registration/signup.html')

def change_password(request):
    return render(request, 'registration/change-password.html')

def reset_password(request):
    pass

def reset_password_done(request):
    pass

def reset_password_confirm(request):
    pass

def reset_password_complete(request):
    pass

def edit_profile(request):
    pass