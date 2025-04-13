from django.urls import path
from mysite.views import UsuarioLoginView
from mysite import views
from django.contrib.auth.views import LogoutView

from .views import (
    home, animales, lugarestf, enemigos, construcciones, flora,
    armas, consumibles, historia, forowiki, registrasewiki,
    inicio_sesion_wiki, micuentatf, recuperarcontra,
    UsuarioLoginView
)

urlpatterns = [
    path("", home, name="home"),
    path("animales", animales, name="animales"),
    path("lugarestf", lugarestf, name="lugarestf"),
    path("enemigos", enemigos, name="enemigos"),
    path("construcciones", construcciones, name="construcciones"),
    path("flora", flora, name="flora"),
    path("armas", armas, name="armas"),
    path("consumibles", consumibles, name="consumibles"),
    path("historia", historia, name="historia"),
    path("forowiki", forowiki, name="forowiki"),
    path("inicio_sesion_wiki", inicio_sesion_wiki, name="inicio_sesion_wiki"),
    path("micuentatf", micuentatf, name="micuentatf"),
    path("recuperarcontra", recuperarcontra, name="recuperarcontra"),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('registrase_wiki/', registrasewiki, name='registrasewiki'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('editar_perfil/', views.editarperfil, name='editar_perfil'),


]
