from django.urls import path
# from . views import services
# from . views import services_details
from .views import ServicesView, ServicesDetaisView

app_name = "services"

urlpatterns = [
    # path('', services, name="services"),
    path('', ServicesView.as_view(), name="services"),
    # path('category/<str:category>', services, name="category"),
    path('category/<str:category>', ServicesView.as_view(), name="category"),
    path('details/<int:pk>', ServicesDetaisView.as_view(), name="services-details"),
]