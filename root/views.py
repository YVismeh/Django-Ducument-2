from django.shortcuts import render
from .models import Testimonials, ContactUs
from services.models import Services
from .forms import ContactUsForm
from django.contrib import messages


# Create your views here.

def home(request):
    services = Services.objects.all()[:2]
    testimonials = Testimonials.objects.all()

    context = {
        "testimonials": testimonials,
        "services": services,
    }

    if request.method == "POST" :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "successfully created contact")
            return render(request, 'root/index.html', context = context)
        else:
            messages.add_message(request, messages.ERROR, "data invalid")
            return render(request, 'root/index.html', context = context)
    else:
        return render(request, 'root/index.html', context = context)
    
    # if request.method == "POST" :
    #     form = ContactUsForm(request.POST)
    #     if form.is_valid():
    #         contact = ContactUs()
    #         contact.name = request.POST.get('name')
    #         contact.email = request.POST.get('email')
    #         contact.subject = request.POST.get('subject')
    #         contact.message = request.POST.get('message')
    #         contact.save()
    #         messages.add_message(request, messages.SUCCESS, "successfully created contact")
    #         return render(request, 'root/index.html', context = context)
    #     else:
    #         messages.add_message(request, messages.ERROR, "data invalid")
    #         return render(request, 'root/index.html', context = context)
    # else:
    #     return render(request, 'root/index.html', context = context)



# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<p>Hello, world. You're at the root index.</p>")