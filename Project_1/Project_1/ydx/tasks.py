from celery import shared_task
import json
import requests
from bs4 import BeautifulSoup
from pytils.translit import translify

from Project_1.settings import *
from .models import YdxWeather


id_city_in_service = 1


@shared_task
def ydx_save_to_base():
    page = requests.get('https://yandex.ru/pogoda/{}'.format(YDX_city))
    soup = BeautifulSoup(page.text, 'html.parser')

    main_info = soup.find(class_='compare-cities-action '
                                 'compare-cities-action_with-tooltip_yes '
                                 'compare-cities-action_contains_no '
                                 'compare-cities-action_action_add '
                                 'compare-cities-action_kind_list-action i-bem').get('data-bem')
    main_info = json.loads(str(main_info))

    id_city = main_info['compare-cities-action']['location']
    name_city = translify(str(main_info['compare-cities-action']['name']))

    temp = str(soup.find(class_='temp__value').contents[0])
    if temp[0] == '+':
        temp = float(temp[1:])
    else:
        temp = float(temp)

    pressure = soup.find(class_='term term_orient_v fact__pressure')
    pressure = round(float(pressure.find(class_='term__value').contents[1])/conv_pressure, 2)
    humidity = soup.find(class_='term term_orient_v fact__humidity')
    humidity = float((humidity.find(class_='term__value').contents[1]).replace('%', ""))

    wind_speed = float(str(soup.find(class_='wind-speed').contents[0]).replace(',', '.'))

    ans = YdxWeather(id_city=id_city,
                     id_city_in_service=id_city_in_service,
                     name_city=name_city,
                     temp=temp,
                     pressure=pressure,
                     humidity=humidity,
                     wind_speed=wind_speed)
    ans.save()
    return 0
