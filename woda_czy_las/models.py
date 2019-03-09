from django.db import models

# Create your models here.


class WodaInfo(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


class LasInfo(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
