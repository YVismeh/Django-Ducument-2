from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class RootStaticUrls(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            "root:home",
        ]
    
    def location(self, items):
        return reverse(items)