from celery import shared_task
import json
import requests
from bs4 import BeautifulSoup

from Project_1 import settings
from .models import YdxWeather


@shared_task
def ydx_save_to_base():
    page = requests.get('https://yandex.ru/pogoda/{}'.format(settings.YDX_city))
    soup = BeautifulSoup(page.text, 'html.parser')

    temp = str(soup.find(class_='temp__value').contents[0])
    if temp[0] == '+':
        temp = float(temp[1:])
    else:
        temp = float(temp)

    pressure = soup.find(class_='term term_orient_v fact__pressure')
    pressure = round(float(pressure.find(class_='term__value').contents[1])/settings.conv_pressure, 2)
    humidity = soup.find(class_='term term_orient_v fact__humidity')
    humidity = float((humidity.find(class_='term__value').contents[1]).replace('%', ""))

    ans = YdxWeather(id_city=settings.id_city,
                     temp=temp,
                     pressure=pressure,
                     humidity=humidity)
    ans.save()
    return 0
