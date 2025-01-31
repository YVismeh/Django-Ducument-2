from django.contrib import admin
from .models import Services, SpecialService, Category, Comments

# Register your models here.

admin.site.register(SpecialService)
admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Comments)