from django.shortcuts import render
from .data.cards_data import cards_data
from .data.pueblos_data import pueblos_data
from .data.ubicaciones_especificas_data import ubicaciones_especificas_data
from .data.ubicaciones_variadas_data import ubicaciones_variadas_data
from .data.animales_data import animales_data


# Create your views here.
def home(request):
    return render(request, "menuprincipal_wiki.html", {"cards": cards_data})


def animales(request):
    return render(request, "Animales.html", {"animales": animales_data})


def lugarestf(request):

    return render(
        request,
        "Lugarestf.html",
        {
            "pueblos": pueblos_data,
            "ubicaciones_especificas": ubicaciones_especificas_data,
            "ubicaciones_variadas": ubicaciones_variadas_data,
        },
    )


def enemigos(request):
    return render(request, "Enemigos.html")


def construcciones(request):
    return render(request, "Construcciones.html")


def flora(request):
    return render(request, "Flora.html")


def armas(request):
    return render(request, "Armas.html")


def consumibles(request):
    return render(request, "Consumibles.html")


def historia(request):
    return render(request, "historia.html")


def forowiki(request):
    return render(request, "forowiki.html")


def registrasewiki(request):
    return render(request, "registrase_wiki.html")


def inicio_sesion_wiki(request):
    return render(request, "inicio_sesion_wiki.html")


def micuentatf(request):
    return render(request, "micuentatf.html")
