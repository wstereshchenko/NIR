from django.db import models


class OwmWeather(models.Model):
    id_city = models.IntegerField()
    temp = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)
