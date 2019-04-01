from django.http import JsonResponse
import requests
import json
from pytils.translit import translify
from bs4 import BeautifulSoup

from Project_1.settings import *


def current_temp(request):
    page = requests.get('https://yandex.ru/pogoda/{}'.format(YDX_city))
    soup = BeautifulSoup(page.text, 'html.parser')

    main_info = soup.find(class_='compare-cities-action '
                                 'compare-cities-action_with-tooltip_yes '
                                 'compare-cities-action_contains_no '
                                 'compare-cities-action_action_add '
                                 'compare-cities-action_kind_list-action i-bem').get('data-bem')
    main_info = json.loads(str(main_info))

    id_city = str(main_info['compare-cities-action']['location'])
    name_city = translify(str(main_info['compare-cities-action']['name']))

    temp = str(soup.find(class_='temp__value').contents[0])
    if temp[0] == '+':
        temp = temp[1:]


    wind_speed = str(soup.find(class_='wind-speed').contents[0])

    #0,750063755419211
    print(wind_speed)
    return JsonResponse({'msg': 'ok'}, status=200)
