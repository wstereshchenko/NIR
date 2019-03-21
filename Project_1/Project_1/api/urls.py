from django.urls import path, include


urlpatterns = [
    path('owp/', include("owm.urls"))
]
