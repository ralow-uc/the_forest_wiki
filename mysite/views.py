from django.shortcuts import render, redirect
from .data.cards_data import cards_data
from .data.pueblos_data import pueblos_data
from .data.ubicaciones_especificas_data import ubicaciones_especificas_data
from .data.ubicaciones_variadas_data import ubicaciones_variadas_data
from .data.animales_data import animales_data
from .data.enemigos_data import enemigos_data
from .data.armas_data import armas_data
from .data.flora_data import flora_data
from .data.consumibles_data import consumibles_data
from .data.historia_data import historia_slider, historia_texto
from .data.micuentatf_data import micuentatf_data
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout


# Importación de Modelos
from .models import Construccion


@login_required
def home(request):
    return render(request, "menuprincipal_wiki.html", {"cards": cards_data})

@login_required
def animales(request):
    return render(request, "Animales.html", {"animales": animales_data})

@login_required
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

@login_required
def enemigos(request):
    return render(request, "Enemigos.html", {"enemigos": enemigos_data})

@login_required
def construcciones(request):
    construcciones = Construccion.objects.all()
    return render(request, "Construcciones.html", {"construcciones": construcciones})

@login_required
def flora(request):
    return render(request, "Flora.html", {"flora": flora_data})

@login_required
def armas(request):
    return render(request, "Armas.html", {"armas": armas_data})

@login_required
def consumibles(request):
    return render(request, "Consumibles.html", {"consumibles": consumibles_data})

@login_required
def historia(request):
    return render(
        request,
        "historia.html",
        {"historia_slider": historia_slider, "historia_texto": historia_texto},
    )

@login_required
def forowiki(request):
    return render(request, "forowiki.html")


def inicio_sesion_wiki(request):
    return render(request, "inicio_sesion_wiki.html")

@login_required
def micuentatf(request):
    return render(request, "micuentatf.html", {
        "micuenta": request.user
    })


def recuperarcontra(request):
    return render(request, "recuperarcontra.html")


def registrase(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada exitosamente!")
            return redirect("home")
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = CustomUserCreationForm()

    return render(request, "registrase_wiki.html", {"form": form})


from django.contrib.auth import authenticate, login


def inicio_sesion_wiki(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "inicio_sesion_wiki.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio_sesion_wiki")
