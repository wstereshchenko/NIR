from django.http import JsonResponse
from Project_1 import settings

import requests
from bs4 import BeautifulSoup


def current_temp(request):
    page = requests.get('https://beta.gismeteo.ru/weather-{}-{}/now/'.format(settings.GISM_city, settings.GISM_city_id))
    soup = BeautifulSoup(page.text, 'html.parser')

    temp = str(soup.find(class_='nowvalue__text_l').contents[0])[-8]
    temp = temp + str(soup.find(class_='nowvalue__text_l').contents[1]).replace(' ', '')
    temp = temp.replace(',', '.')
    if temp[0] == '+':
        temp = float(temp[1:])
    else:
        temp = float(temp)

    pressure = float(soup.find(class_='unit unit_pressure_h_pa').find(class_='nowinfo__value').contents[0])

    humidity = float(soup.find(class_='nowinfo__item nowinfo__item_humidity').find(class_='nowinfo__value').contents[0])

    ans = {'id_city': settings.id_city,
           'temp': temp,
           'pressure': pressure,
           'humidity': humidity}
    return JsonResponse(ans, status=200)
