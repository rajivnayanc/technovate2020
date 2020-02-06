from django.db import models

# Create your models here.

class Cultural(models.Model):
    event_name = models.CharField(max_length=255)
    event_brief_desc = models.TextField(blank=True, null=True)
    event_quote = models.TextField(blank=True, null=True)
    event_quote_author = models.CharField(max_length=255, null=True, blank=True)
    event_1_Prize = models.CharField(max_length=255,blank=True, null=True)
    event_2_Prize = models.CharField(max_length=255,blank=True, null=True)
    event_3_Prize = models.CharField(max_length=255,blank=True, null=True)
    event_reg_active = models.BooleanField(default=True)
    event_fees = models.CharField(max_length=50, blank=True, null=True)
    event_description = models.TextField(blank = True, null = True)
    event_head = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    description_file = models.FileField(upload_to='cultural_docs', max_length=100)
    event_logo  = models.ImageField(upload_to='cultural_logo', height_field=None, width_field=None, max_length=None)
    url = models.URLField(max_length=30,blank=True)
    def __str__(self):
        return self.event_name
    

class Technical(models.Model):
    event_name = models.CharField(max_length=255)
    event_brief_desc = models.TextField(blank=True, null=True)
    event_quote = models.TextField(blank=True, null=True)
    event_quote_author = models.CharField(max_length=255, null=True, blank=True)
    event_1_Prize = models.CharField(max_length = 255,blank=True, null=True)
    event_2_Prize = models.CharField(max_length = 255,blank=True, null=True)
    event_3_Prize = models.CharField(max_length = 255,blank=True, null=True)
    event_reg_active = models.BooleanField(default=True)
    event_fees = models.CharField(max_length=50, blank=True, null=True)
    event_description = models.TextField(blank = True, null = True)
    event_head = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    description_file = models.FileField(upload_to='technical_docs', max_length=100)
    event_logo  = models.ImageField(upload_to='technical_logo', height_field=None, width_field=None,max_length=None)
    url = models.URLField(max_length=30, blank=True)
    def __str__(self):
        return self.event_name


class Informal(models.Model):
    event_name = models.CharField(max_length=255)
    event_brief_desc = models.TextField(blank=True, null=True)
    event_quote = models.TextField(blank=True, null=True)
    event_quote_author = models.CharField(max_length=255, null=True,blank=True)
    event_1_Prize = models.CharField(max_length=255, blank=True, null=True)
    event_2_Prize = models.CharField(max_length=255,blank=True, null=True)
    event_3_Prize = models.CharField(max_length=255,blank=True, null=True)
    event_reg_active = models.BooleanField(default=True)
    event_fees = models.CharField(max_length=50,blank=True,null=True)
    event_description = models.TextField(blank=True, null=True)
    event_head = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    description_file = models.FileField(upload_to='informal_docs', max_length=100)
    event_logo = models.ImageField(upload_to='informal_logo', height_field=None,width_field=None, max_length=None,)
    url = models.URLField(max_length=30, blank=True)
    def __str__(self):
        return self.event_name


