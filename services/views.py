from django.shortcuts import render, get_object_or_404, redirect
from . models import Services, Comments
from django.core.paginator import Paginator
from .forms import CommentsForm
from django.contrib import messages


# Create your views here.

# CBV services

from django.views.generic import ListView
class ServicesView(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = "services"
    # paginator
    paginate_by = 2
    # queryset = Services.objects.filter(status=True)

    def get_queryset(self):
        if self.kwargs.get("category"):
            services = self.model.objects.filter(category__title=self.kwargs.get("category"))
            # service = Services.objects.filter(category__title=self.kwargs.get("category"))
        else:
            services = Services.objects.filter(status=True)
        return services
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = 1
        services_paginate = Paginator(self.get_queryset(), 2)
        last = services_paginate.num_pages
        context["first"] = first
        context["last"] = last
        
        return context





# FBV services

# def services(request, category=None):
#     if category is None:
#         services = Services.objects.all()
#     else:
#         services = Services.objects.filter(category__title=category)

#     services_paginate = Paginator(services, 2)
#     first_page = 1
#     last_page = services_paginate.num_pages

#     try:
#         page_number = request.GET.get("page")
#         services = services_paginate.get_page(page_number)
#     except:
#         page_number = first_page
#         services = services_paginate.get_page(first_page)


#     context = {
#         "services": services,
#         "first": first_page,
#         "last": last_page,
#     }
#     return render(request, 'services/services.html', context=context)



# CBV srevice detais

from django.views.generic import DetailView

class ServicesDetaisView(DetailView):
    model = Services
    template_name = 'services/service-details.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs["pk"]
        service = get_object_or_404(Services, id=id)
        context = super().get_context_data(**kwargs)
        context["form"] = CommentsForm()
        context["comments"] = Comments.objects.filter(status=True, service=service.id)
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                id = self.kwargs["pk"]
                service = get_object_or_404(Services, id=id)
                comment = form.save(commit=False)
                comment.service = service
                comment.save()
                messages.add_message(self.request, messages.SUCCESS, "successfully sent")
                return redirect(self.request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(self.request.path_info)
        else:
            return redirect("accounts:login")

    # def form_valid(self, form, **kwargs):
    #     id = self.kwargs["pk"]
    #     service = get_object_or_404(Services, id=id)
    #     comment = form.save(commit=False)
    #     comment.service = service
    #     comment.save()
    #     messages.add_message(self.request, messages.SUCCESS, "successfully sent")
    #     return redirect(self.request.path_info)
    
    


# FBV srevice detais

# def services_details(request, id=None):
#     service = get_object_or_404(Services, id=id)
#     form = CommentsForm(request.POST)
#     comments = Comments.objects.filter(status=True, service=service.id)

#     context = {
#             "services": service,
#             "form": form,
#             "comments": comments,
#         }

#     if request.method == "POST":
#         form = CommentsForm(request.POST)
#         if request.user.is_authenticated:
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.service = service
#                 comment.save()
#                 messages.add_message(request, messages.SUCCESS, "successfully sent")
#                 return render(request, 'services/service-details.html', context=context)
            
#             else:
#                 messages.add_message(request, messages.ERROR, "invalid data")
#                 return render(request, 'services/service-details.html', context=context)
#         else:
#             return redirect("accounts:login")

#     else:
#         return render(request, 'services/service-details.html', context=context)