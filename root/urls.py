from django.urls import path
from . views import home

app_name = "root"

urlpatterns = [
    path('', home, name="home"),
    path('/#contact', home, name="contact"),
    path('/#about', home, name="about"),
]