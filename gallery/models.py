from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', height_field=None, width_field=None, max_length=None)
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption
    
