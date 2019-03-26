from django.urls import path, include


urlpatterns = [
    path('owm/', include("owm.urls"))
]
