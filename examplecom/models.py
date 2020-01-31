from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    description = 'a'


# Create your models here.
