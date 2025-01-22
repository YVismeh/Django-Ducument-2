from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'root/index.html')



# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<p>Hello, world. You're at the root index.</p>")