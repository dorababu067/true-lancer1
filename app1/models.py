from django.db import models

# Create your models here.
class CaronaData(models.Model):
    country = models.CharField(max_length=250, null=True, blank=True)
    population = models.CharField(max_length=250, null=True, blank=True)
    cases = models.CharField(max_length=250, null=True, blank=True)
    deaths = models.CharField(max_length=250, null=True, blank=True)
    day = models.CharField(max_length=250, null=True, blank=True)
    time = models.CharField(max_length=250, null=True, blank=True)
    current_time = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.country

class Asset(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.name