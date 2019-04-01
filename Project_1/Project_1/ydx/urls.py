from django.urls import path
from .views import current_temp


urlpatterns = [
    path('current-temp/', current_temp)
]
