from celery import shared_task
import requests
from bs4 import BeautifulSoup

from Project_1.settings import *
from .models import GismWeather


id_city_in_service = 1


@shared_task
def gism_save_to_base():
    page = requests.get('https://beta.gismeteo.ru/weather-{}-{}/now/'.format(GISM_city, GISM_city_id))
    soup = BeautifulSoup(page.text, 'html.parser')

    id_city = GISM_city_id
    name_city = GISM_city

    temp = str(soup.find(class_='nowvalue__text_l').contents[0])[-8]
    temp = temp + str(soup.find(class_='nowvalue__text_l').contents[1]).replace(' ', '')
    if temp[0] == '+':
        temp = float(temp[1:])
    else:
        temp = float(temp)

    pressure = float(soup.find(class_='unit unit_pressure_h_pa').find(class_='nowinfo__value').contents[0])

    humidity = float(soup.find(class_='nowinfo__item nowinfo__item_humidity').find(class_='nowinfo__value').contents[0])

    ans = GismWeather(id_city=id_city,
                      id_city_in_service=id_city_in_service,
                      name_city=name_city,
                      temp=temp,
                      pressure=pressure,
                      humidity=humidity)
    ans.save()
    return 0
