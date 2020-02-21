from django.db import models

# Create your models here.
class Celeb_Images(models.Model):
    image = models.ImageField(upload_to='celeb_night', height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=255,blank=True)
    desc = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.title
    