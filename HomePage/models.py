from django.db import models

# Create your models here.

class Links(models.Model):
    url = models.URLField(blank=True)
    price = models.CharField(max_length = 255,blank =True)

    def __str__(self):
        return self.url
    