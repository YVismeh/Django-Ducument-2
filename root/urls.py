from django.urls import path
from . views import home, login, signup, forget_password

app_name = "root"

urlpatterns = [
    path('', home, name="home"),
]