from django.db import models


class GismWeather(models.Model):
    id_city = models.IntegerField()
    id_city_in_service = models.IntegerField()
    name_city = models.CharField(max_length=50)
    temp = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)