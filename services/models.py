from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title

class SpecialService(models.Model):
    title = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField()
    special_service = models.ForeignKey(SpecialService, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    img = models.ImageField(upload_to="services", default="default.jpg")
    catalog_pdf = models.TextField()
    catalog_doc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.desc[:200] 
    