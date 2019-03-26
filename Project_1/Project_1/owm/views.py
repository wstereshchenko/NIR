from django.http import JsonResponse
import requests

from Project_1.settings import *
from owm.tasks import owm_save_to_base


def current_temp(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units={}&appid={}'
                            .format(OWP_id_city, OWP_units, OWP_appid)).json()

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

    ok = owm_save_to_base.delay()
    return JsonResponse({'msg': 'ok'}, status=200)
