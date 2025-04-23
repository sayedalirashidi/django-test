
from django.db import models

class blog(models.Model):
    title = models.CharField (max_length = 100)
    author = models.CharField (max_length = 100)
    date = models.DateField ()
    link = models.URLField ()