from celery import shared_task
import requests

from Project_1 import settings
from .models import OwmWeather


id_city_in_service = 1


@shared_task
def owm_save_to_base():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units={}&appid={}'
                            .format(settings.OWP_id_city, settings.OWP_units, settings.OWP_appid)).json()
    ans = OwmWeather(id_city=settings.id_city,
                     temp=response['main']['temp'],
                     pressure=response['main']['pressure'],
                     humidity=response['main']['humidity'])
    ans.save()
    return 0
