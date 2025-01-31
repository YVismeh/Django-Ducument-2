from django.db import models

# Create your models here.

class Score(models.Model):
    count = models.IntegerField(default=5)

    def __str__(self):
        return str(self.count)
    
class Testimonials(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="tester", default="default.jpg")
    content = models.TextField()
    domain = models.CharField(max_length=30)
    stars = models.ForeignKey(Score, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def stars_count(self):
        return range(self.stars.count)
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name