from django.http import JsonResponse
import requests

from Project_1 import vrb
from .tasks import aaa
from .models import OwmWeather


def current_temp(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units={}&appid={}'
                            .format(vrb.OWP_id_city, vrb.OWP_units, vrb.OWP_appid)).json()

    # print("id_city: {}".format(response['id']))
    # print("name_city: {}".format(response['name']))
    # print("lon: {}".format(response['coord']['lon']))
    # print("lat: {}".format(response['coord']['lat']))
    # print("temp: {}".format(response['main']['temp']))
    # print("pressure: {}".format(response['main']['pressure']))
    # print("humidity: {}".format(response['main']['humidity']))
    # print("wind_speed: {}".format(response['wind']['speed']))
    # print("wind_deg: {}".format(response['wind']['deg']))
    # print("date_time: {}".format(response['dt'])

    # ans = OwmWeather(id_city=response['id'],
    #                  name_city=response['name'],
    #                  lon=response['coord']['lon'],
    #                  lat=response['coord']['lat'],
    #                  temp=response['main']['temp'],
    #                  pressure=response['main']['pressure'],
    #                  humidity=response['main']['humidity'],
    #                  wind_speed=response['wind']['speed'],
    #                  wind_deg=response['wind']['deg'])
    # ans.save()
    # aaa.delay()
    return JsonResponse({'msg': 'ok'}, status=200)
