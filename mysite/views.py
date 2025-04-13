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
from .data.micuentatf_data import micuentatf_data
from .models import Rol
from .forms import RegistroUsuarioForm
from django.contrib import messages
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import EditarPerfilForm


# Importación de Modelos
from .models import Construccion


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
    construcciones = Construccion.objects.all()
    return render(request, "Construcciones.html", {"construcciones": construcciones})


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
    if request.user.is_authenticated:
        return render(request, "micuentatf.html", {"micuenta": request.user})
    else:
        return redirect("login")


def recuperarcontra(request):
    return render(request, "recuperarcontra.html")


def registrasewiki(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if Usuario.objects.filter(username=username).exists():
                messages.error(request, 'Ese nombre de usuario ya existe.')
            elif Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Ese correo ya está registrado.')
            else:
                usuario = Usuario(
                    username=username,
                    email=email,
                    password=make_password(password1)
                )
                rol_usuario = Rol.objects.get(nombre='Usuario')
                usuario.rol = rol_usuario
                usuario.save()
                messages.success(request, 'Usuario creado correctamente.')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')

    return render(request, 'registrase_wiki.html')


def inicio_sesion_wiki(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Intenta nuevamente.')

    return render(request, 'inicio_sesion_wiki.html')

class UsuarioLoginView(LoginView):
    template_name = 'inicio_sesion_wiki.html'


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario

@login_required
def editarperfil(request):
    usuario = request.user

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif password1 and not (any(c.islower() for c in password1) and any(c.isupper() for c in password1) and any(c.isdigit() for c in password1) and len(password1) >= 8):
            messages.error(request, 'La contraseña no cumple con los requisitos de seguridad.')
        else:
            usuario.username = username
            usuario.email = email
            if password1:
                usuario.password = make_password(password1)
            usuario.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('micuentatf')

    return render(request, 'editarperfil.html', {
        'username': usuario.username,
        'email': usuario.email,
    })
