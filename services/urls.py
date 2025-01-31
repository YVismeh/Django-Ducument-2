from django.urls import path
from . views import services, services_details

app_name = "services"

urlpatterns = [
    path('', services, name="services"),
    path('category/<str:category>', services, name="category"),
    path('details/<int:id>', services_details, name="services-details"),
]