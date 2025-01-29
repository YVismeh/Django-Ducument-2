from django.contrib import admin
from .models import Services, SpecialService, Category

# Register your models here.

admin.site.register(SpecialService)
admin.site.register(Category)
admin.site.register(Services)