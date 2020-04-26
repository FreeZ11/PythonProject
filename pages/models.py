from django.db import models

# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=1200)
    subscriptions = models.DecimalField(max_digits=10000000, decimal_places=1)
    videos = models.DecimalField(max_digits=1000000, decimal_places=1)
    views = models.DecimalField(max_digits=10000000, decimal_places=1)
