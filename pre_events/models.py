from django.db import models

# Create your models here.

class PreEvent(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.TextField()
    event_poster = models.ImageField(upload_to='pre_event_poster', height_field=None, width_field=None, max_length=None)
    event_link = models.URLField(max_length=200)
    event_date = models.CharField(max_length=50)

    def __str__(self):
        return self.event_name
    
