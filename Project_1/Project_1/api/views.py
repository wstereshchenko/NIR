from django.http import JsonResponse
import requests
import time



appid = '6701628c6e670a9fa0d12355d365e57f'
id_city = '484907'
units = 'metric'


def current_temp(request):
    res = dict()
    response = requests.get('https://api.openweathermap.org/data/2.5/forecast/daily?id={}&mode=json&units={}&cnt=7&appid={}'
                            .format(id_city, units, appid)).json()
    for _id in range(len(response['list'])):
        data = time.gmtime(response['list'][_id]['dt'])
        data = time.strftime('%d-%m-%Y', data)
        res[data] = response['list'][_id]['temp']['day']
    print(res)
    return JsonResponse({'msg': 'ok'}, status=200)
