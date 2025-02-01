from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Services

# static
class ServicesStaticUrls(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            "services:services",
        ]
    
    def location(self, items):
        return reverse(items)
    
# dynamic
class ServicesDynamicUrls(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return  Services.objects.all()
    
    def location(self, items):
        return "services/detail/%i" % items.id