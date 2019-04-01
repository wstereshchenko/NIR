from celery import shared_task
import requests

from Project_1.settings import *
from owm.models import OwmWeather


@shared_task
def owm_save_to_base():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units={}&appid={}'
                            .format(OWP_id_city, OWP_units, OWP_appid)).json()
    ans = OwmWeather(id_city=response['id'],
                     name_city=response['name'],
                     lon=response['coord']['lon'],
                     lat=response['coord']['lat'],
                     temp=response['main']['temp'],
                     pressure=response['main']['pressure'],
                     humidity=response['main']['humidity'],
                     wind_speed=response['wind']['speed'],
                     wind_deg=response['wind']['deg'])
    ans.save()
    return 0
