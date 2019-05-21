from django.http import JsonResponse
from Project_1 import settings
import requests


def current_temp(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?id={}&mode=json&units={}&appid={}'
                            .format(settings.OWP_id_city, settings.OWP_units, settings.OWP_appid)).json()
    ans = {'id_city': settings.id_city,
           'temp': response['main']['temp'],
           'pressure': response['main']['pressure'],
           'humidity': response['main']['humidity']}
    return JsonResponse(ans, status=200)
