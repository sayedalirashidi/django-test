from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField (max_length=100)
    date = models.DateField ()
    number = models.IntegerField ()
    author = models.CharField(max_length=100)
    
    