from django.shortcuts import render
from .data.cards_data import cards_data
from .data.pueblos_data import pueblos_data
from .data.ubicaciones_especificas_data import ubicaciones_especificas_data
from .data.ubicaciones_variadas_data import ubicaciones_variadas_data
from .data.animales_data import animales_data
from .data.enemigos_data import enemigos_data
from .data.construcciones_data import construcciones_data
from .data.armas_data import armas_data
from .data.flora_data import flora_data
from .data.consumibles_data import consumibles_data
from .data.historia_data import historia_slider, historia_texto
from .data.micuentaf_data import micuentaf_data

def micuenta(request):
    return render(request, "micuentatf.html", {"micuenta": micuentaf_data})


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
    return render(request, "Enemigos.html", {"enemigos": enemigos_data})


def construcciones(request):
    return render(request, "Construcciones.html", {"construcciones": construcciones_data})


def flora(request):
    return render(request, "Flora.html", {"flora": flora_data})


def armas(request):
    return render(request, "Armas.html", {"armas": armas_data})


def consumibles(request):
    return render(request, "Consumibles.html", {"consumibles": consumibles_data})


def historia(request):
    return render(request, "historia.html", {
        "historia_slider": historia_slider,
        "historia_texto": historia_texto
    })


def forowiki(request):
    return render(request, "forowiki.html")


def registrasewiki(request):
    return render(request, "registrase_wiki.html")


def inicio_sesion_wiki(request):
    return render(request, "inicio_sesion_wiki.html")


def micuentatf(request):
    return render(request, "micuentatf.html",{"micuenta": micuentaf_data})
