from django.shortcuts import render, get_object_or_404
from . models import Services, Category, SpecialService

# Create your views here.

def services(request):
    services = Services.objects.all()
    context = {
        "services": services
    }
    return render(request, 'services/services.html', context=context)

def services_details(request, id=None):
    service = get_object_or_404(Services, id=id)
    category = Category.objects.all()
    s_services = SpecialService.objects.filter(status=True)
    context = {
        "services": service,
        "category": category,
        "s_services": s_services,
    }

    return render(request, 'services/service-details.html', context=context)