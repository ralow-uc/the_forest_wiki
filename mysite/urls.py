from django.urls import path
from .views import home, animales, lugarestf, enemigos, construcciones, flora, armas, consumibles, historia

urlpatterns = [
    path('', home, name='home'),
    path('animales', animales, name='animales'),
    path('lugarestf', lugarestf, name='lugarestf'),
    path('enemigos', enemigos, name='enemigos'),
    path('construcciones', construcciones, name='construcciones'),
    path('flora', flora, name='flora'),
    path('armas', armas, name='armas'),
    path('consumibles', consumibles, name='consumibles'),
    path('historia', historia, name='historia'),
]
