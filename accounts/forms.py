from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from captcha.fields import CaptchaField

class Captcha(forms.Form):
    captcha = CaptchaField()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=120, widget=forms.PasswordInput)
    captcha = CaptchaField()

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

class ChangePassForm(forms.Form):
    password1 = forms.CharField(max_length=15)
    password2 = forms.CharField(max_length=15)

class ResetPassEmailForm(forms.Form):
    email = forms.EmailField()

class ResetPassForm(forms.Form):
    pass1 = forms.CharField(max_length=15)
    pass2 = forms.CharField(max_length=15)

class EditeProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["id_code", "phone", "image", "username", "address"]