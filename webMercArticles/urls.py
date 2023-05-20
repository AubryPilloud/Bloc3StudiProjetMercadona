from django.urls import path

from .views import *


urlpatterns = [
    path('', accueil_view),
    path('catalogue/', catalogue, name='catalogue')
]