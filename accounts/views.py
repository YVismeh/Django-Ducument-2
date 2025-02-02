from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, Captcha, ChangePassForm, ResetPassForm, ResetPassEmailForm, EditeProfile
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import password_validation
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from . models import User, Profile

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = request.POST.get('username').strip()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('root:home')
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(request.path_info)
        else:
                messages.add_message(request, messages.ERROR, "invalid captcha")
                return redirect(request.path_info)
     
    else:
        context = {
            "form" : Captcha()
        }
        return render(request, 'registration/login.html', context=context)

@login_required
def logout_user(request):
    logout(request)
    return redirect("root:home")

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.email = form.cleaned_data["email"]
            # form.save()
            user = form.save()
            login(request, user)
            return redirect("root:home")
        else:
            messages.add_message(request, messages.ERROR, "invalid data")
            return redirect(request.path_info)
    else:
        
        return render(request, 'registration/signup.html')


@login_required
def change_password(request):
    user = request.user
    if request.method == "POST":
        form = ChangePassForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data["password1"]
            pass2 = form.cleaned_data["password2"]
            if (pass1==pass2) and not (user.check_password(pass1)):
                try:
                    password_validation.validate_password(pass1)
                except:
                    messages.add_message(request, messages.ERROR, "Invalid password")
                    return redirect(request.path_info) 
                else:
                    user.set_password(pass1)
                    user.save()
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "successfully changed password")        
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "pass1 and pass2 are'n similar or different with old one")  
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "Invalid data")  
            return redirect(request.path_info)

    else:
        return render(request, 'registration/change-password.html')

def reset_password(request):
    if request.method == "POST":
        form = ResetPassEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
            except:
                messages.add_message(request, messages.ERROR, "email not found")  
                return redirect(request.path_info)
            else:
                token, create = Token.objects.get_or_create(user=user)
                if not create:
                    Token.objects.get(user=user).delete()
                    token = Token.objects.create(user=user)
                send_mail(
                    "reset UR password",
                    f"https://127.0.0.1:8000/accounts/reset-password-confirm/{token.key}",
                    "admin@mysite.com",
                    [user.email],
                    fail_silently=True,
                )
                return redirect("accounts:reset_password_done")
        else:
            messages.add_message(request, messages.ERROR, "Invalid data")  
            return redirect(request.path_info)

    else:
        return render(request, 'registration/reset-password.html')


def reset_password_done(request):
    return render(request, 'registration/reset-password-done.html')


def reset_password_confirm(request, token):
    if request.method == 'POST':
        user = Token.objects.get(key=token).user
        form = ResetPassForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data["pass1"]
            pass2 = form.cleaned_data["pass2"]
            if (pass1==pass2) and not (user.check_password(pass1)):
                try:
                    password_validation.validate_password(pass1)
                except:
                    messages.add_message(request, messages.ERROR, "Invalid password")
                    return redirect(request.path_info) 
                else:
                    user.set_password(pass1)
                    user.save()
                    return redirect("accounts:reset_password_complete")
            else:
                messages.add_message(request, messages.ERROR, "pass1 and pass2 are'n similar or different with old one")  
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "Invalid data")  
            return redirect(request.path_info)
    else:
        return render(request, 'registration/reset-password-confirm.html')



def reset_password_complete(request):
    return render(request, 'registration/reset-password-compleete.html')


# @login_required
# def edit_profile(request, id):
#     user_profile = Profile.objects.get(user=id)
#     if request.method == "POST":
#         form = EditeProfile(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
#             return redirect(request.path_info)
#         else:
#             messages.add_message(request, messages.ERROR, "Invalid input data")
#             return redirect(request.path_info)
#     else:
        
#         form = EditeProfile(instance=user_profile)
#         context = {
#             "form": form,
#         }
#         return render (request, "registration/edit-profile.html", context=context)