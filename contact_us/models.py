from django.db import models

# Create your models here.

class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    institute  = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name+','+self.institute
    