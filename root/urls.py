from django.urls import path
# from . views import home
from .views import HomeView
from . views import contact_us
from django.views.generic import RedirectView


app_name = "root"

urlpatterns = [
    # path('', home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('contactus', contact_us, name="contactus"),
    path('google', RedirectView.as_view(url="https://google.com"), name="google"), # you can do the same thin with making, for example GoogleView class in views and use it here
]