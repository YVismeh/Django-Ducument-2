from django.shortcuts import render, get_object_or_404
from . models import Services, Category, SpecialService, Comments
from django.core.paginator import Paginator
from .forms import CommentsForm
from django.contrib import messages


# Create your views here.

def services(request, category=None):
    if category is None:
        services = Services.objects.all()
    else:
        services = Services.objects.filter(category__title=category)

    services_paginate = Paginator(services, 2)
    first_page = 1
    last_page = services_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        services = services_paginate.get_page(page_number)
    except:
        page_number = first_page
        services = services_paginate.get_page(first_page)


    context = {
        "services": services,
        "first": first_page,
        "last": last_page,
    }
    return render(request, 'services/services.html', context=context)

def services_details(request, id=None):
    service = get_object_or_404(Services, id=id)
    s_services = SpecialService.objects.filter(status=True)
    comments = Comments.objects.filter(status=True, service=service)
    form = CommentsForm()

    context = {
            "services": service,
            "s_services": s_services,
            "form": form,
            "comments": comments
        }

    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.service = service
            comment.save()
            messages.add_message(request, messages.SUCCESS, "successfully sent")
            return render(request, 'services/service-details.html', context=context)
        
        else:
            messages.add_message(request, messages.ERROR, "invalid data")
            return render(request, 'services/service-details.html', context=context)

    else:
        return render(request, 'services/service-details.html', context=context)