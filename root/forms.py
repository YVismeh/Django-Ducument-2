from django import forms
from .models import ContactUs

# class ContactUsForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "subject", "email", "message"]