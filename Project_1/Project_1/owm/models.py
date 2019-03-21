from django.db import models


class OwmWeather(models.Model):
    id_city = models.IntegerField()
    name_city = models.CharField(max_length=50)
    lon = models.FloatField()
    lat = models.FloatField()
    temp = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)
