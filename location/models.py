from django.db import models

# Create your models here.
class Location(models.Model):
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    post_code =models.IntegerField()