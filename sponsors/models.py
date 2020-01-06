from django.db import models

# Create your models here.

class SponsorType(models.Model):
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.types 

class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    types = models.ForeignKey(SponsorType,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='sponsors_logo', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name 


class SponsorContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
    

    
    
