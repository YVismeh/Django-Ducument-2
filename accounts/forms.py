from django import forms
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField

# class Captcha(forms.Form):
#     captcha = CaptchaField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120, widget=forms.PasswordInput)
    #captcha = CaptchaField()

class SignUpForm(UserCreationForm):
    email = forms.EmailField()