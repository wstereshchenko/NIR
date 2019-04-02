from django.http import JsonResponse


def current_temp(request):

    return JsonResponse({'msg': 'ok'}, status=200)
