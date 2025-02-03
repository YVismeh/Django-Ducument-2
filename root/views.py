from django.shortcuts import render
from .models import Testimonials, ContactUs
from services.models import Services
from .forms import ContactUsForm
from django.contrib import messages


# Create your views here.



# CBV home

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# class HomeView(TemplateView, TemplateView):
class HomeView(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonials.objects.all()
        context["services"] = Services.objects.all()[:2]
        return context




# FBV home

# def home(request):
#     services = Services.objects.all()[:2]
#     testimonials = Testimonials.objects.all()

#     context = {
#         "testimonials": testimonials,
#         "services": services,
#     }
#     return render(request, 'root/index.html', context = context)

#####################################################################################

# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<p>Hello, world. You're at the root index.</p>")

#####################################################################################

def contact_us(request):
    if request.method == "POST" :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "successfully created contact")
            return render(request, 'root/contact-us.html')
        else:
            messages.add_message(request, messages.ERROR, "data invalid")
            return render(request, 'root/contact-us.html')
    else:
        return render(request, "root/contact-us.html")

