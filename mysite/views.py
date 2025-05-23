from django.shortcuts import render, redirect, get_object_or_404
from .data.cards_data import cards_data
from .data.animales_data import animales_data
from .data.armas_data import armas_data
from .data.consumibles_data import consumibles_data
from .data.historia_data import historia_slider, historia_texto
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
import requests

from .forms import (
    CustomUserCreationForm,
    ConstruccionForm,
    UserUpdateForm,
    AnimalForm,
    LugarForm,
    EnemigoForm,
    FloraForm,
    ArmaForm,
)
from django.contrib import messages
from django.contrib.auth import logout


# Importación de Modelos
from .models import Construccion, Animal, Lugar, Enemigo, Flora, Arma


@login_required
def home(request):
    return render(request, "menuprincipal_wiki.html", {"cards": cards_data})


@login_required
def animales(request):
    return render(request, "Animales.html", {"animales": animales_data})


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
    edit_mode = request.GET.get("edit") == "true"
    change_password = request.GET.get("change_password") == "true"

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        current_password = request.POST.get("current_password")

        if not request.user.check_password(current_password):
            messages.error(request, "Contraseña actual incorrecta.")
            return redirect("micuentatf")

        if form.is_valid():
            user = form.save()

            # Verifica si se quieren cambiar las contraseñas
            new_pass1 = request.POST.get("new_password1")
            new_pass2 = request.POST.get("new_password2")

            if new_pass1 or new_pass2:
                if new_pass1 != new_pass2:
                    messages.error(request, "Las contraseñas no coinciden.")
                    return redirect("micuentatf?edit=true&change_password=true")
                else:
                    user.set_password(new_pass1)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(
                        request, "Datos y contraseña actualizados correctamente."
                    )
            else:
                user.save()
                messages.success(request, "Datos actualizados correctamente.")

            return redirect("micuentatf")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        "micuentatf.html",
        {
            "micuenta": request.user,
            "form": form,
            "edit_mode": edit_mode,
            "change_password": change_password,
        },
    )


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


# Funciones para Construcciones
@login_required
def construcciones(request):
    construcciones = Construccion.objects.all()
    return render(request, "Construcciones.html", {"construcciones": construcciones})


@user_passes_test(lambda u: u.is_staff)
def eliminar_construccion(request, pk):
    construccion = get_object_or_404(Construccion, pk=pk)
    construccion.delete()
    messages.success(request, "Construcción eliminada correctamente.")
    return redirect("construcciones")


@user_passes_test(lambda u: u.is_staff)
def editar_construccion(request, id):
    construccion = get_object_or_404(Construccion, id=id)

    if request.method == "POST":
        form = ConstruccionForm(request.POST, request.FILES, instance=construccion)
        if form.is_valid():
            form.save()
            messages.success(request, "Construcción actualizada correctamente.")
            return redirect("construcciones")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = ConstruccionForm(instance=construccion)

    return render(
        request,
        "editar_construccion.html",
        {"form": form, "construccion": construccion},
    )


@user_passes_test(lambda u: u.is_staff)
def crear_construccion(request):
    if request.method == "POST":
        form = ConstruccionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Construcción creada exitosamente.")
            return redirect("construcciones")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = ConstruccionForm()

    return render(request, "crear_construccion.html", {"form": form})


# Funciones para Animales
def animales(request):
    animales = Animal.objects.all()
    edit_mode = request.GET.get("edit") == "true"
    return render(
        request,
        "animales.html",
        {
            "animales": animales,
            "edit_mode": edit_mode,
        },
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def crear_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Animal creado exitosamente!")
            return redirect("animales")
    else:
        form = AnimalForm()
    return render(request, "crear_animal.html", {"form": form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def editar_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Animal actualizado exitosamente!")
            return redirect("animales")
    else:
        form = AnimalForm(instance=animal)
    return render(request, "editar_animal.html", {"form": form, "animal": animal})


@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == "POST":
        animal.delete()
        messages.success(request, "Animal eliminado correctamente.")
        return redirect("animales")


def lugares_view(request):
    lugares = Lugar.objects.all()
    edit_mode = request.GET.get("edit") == "true"
    return render(request, "lugares.html", {"lugares": lugares, "edit_mode": edit_mode})


@user_passes_test(lambda u: u.is_staff)
def crear_lugar(request):
    if request.method == "POST":
        form = LugarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Lugar creado exitosamente.")
            return redirect("lugares_view")
    else:
        form = LugarForm()
    return render(request, "crear_lugar.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def editar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    if request.method == "POST":
        form = LugarForm(request.POST, request.FILES, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, "Lugar actualizado correctamente.")
            return redirect("lugares_view")
    else:
        form = LugarForm(instance=lugar)
    return render(request, "editar_lugar.html", {"form": form, "lugar": lugar})


@user_passes_test(lambda u: u.is_staff)
def eliminar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    lugar.delete()
    messages.success(request, "Lugar eliminado correctamente.")
    return redirect("lugares_view")


@login_required
def enemigos(request):
    enemigos = Enemigo.objects.all()
    edit_mode = request.GET.get("edit") == "true"
    return render(
        request, "enemigos.html", {"enemigos": enemigos, "edit_mode": edit_mode}
    )


@user_passes_test(lambda u: u.is_staff)
def crear_enemigo(request):
    if request.method == "POST":
        form = EnemigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Enemigo creado exitosamente!")
            return redirect("enemigos")
    else:
        form = EnemigoForm()
    return render(request, "crear_enemigo.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def editar_enemigo(request, enemigo_id):
    enemigo = get_object_or_404(Enemigo, id=enemigo_id)
    if request.method == "POST":
        form = EnemigoForm(request.POST, request.FILES, instance=enemigo)
        if form.is_valid():
            form.save()
            messages.success(request, "Enemigo actualizado correctamente.")
            return redirect("enemigos")
    else:
        form = EnemigoForm(instance=enemigo)
    return render(request, "editar_enemigo.html", {"form": form, "enemigo": enemigo})


@user_passes_test(lambda u: u.is_staff)
def eliminar_enemigo(request, enemigo_id):
    enemigo = get_object_or_404(Enemigo, id=enemigo_id)
    enemigo.delete()
    messages.success(request, "Enemigo eliminado correctamente.")
    return redirect("enemigos")


@login_required
def flora(request):
    plantas = Flora.objects.all()
    edit_mode = request.GET.get("edit") == "true"
    return render(request, "flora.html", {"flora": plantas, "edit_mode": edit_mode})


@user_passes_test(lambda u: u.is_staff)
def crear_flora(request):
    if request.method == "POST":
        form = FloraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Planta creada exitosamente.")
            return redirect("flora")
    else:
        form = FloraForm()
    return render(request, "crear_flora.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def editar_flora(request, flora_id):
    planta = get_object_or_404(Flora, id=flora_id)
    if request.method == "POST":
        form = FloraForm(request.POST, request.FILES, instance=planta)
        if form.is_valid():
            form.save()
            messages.success(request, "Planta actualizada correctamente.")
            return redirect("flora")
    else:
        form = FloraForm(instance=planta)
    return render(request, "editar_flora.html", {"form": form, "planta": planta})


@user_passes_test(lambda u: u.is_staff)
def eliminar_flora(request, flora_id):
    planta = get_object_or_404(Flora, id=flora_id)
    planta.delete()
    messages.success(request, "Planta eliminada correctamente.")
    return redirect("flora")


@login_required
def armas(request):
    armas = Arma.objects.all()
    edit_mode = request.GET.get("edit") == "true"
    return render(
        request,
        "armas.html",
        {
            "armas": armas,
            "edit_mode": edit_mode,
        },
    )


@user_passes_test(lambda u: u.is_staff)
def crear_arma(request):
    if request.method == "POST":
        form = ArmaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Arma creada exitosamente.")
            return redirect("armas")
    else:
        form = ArmaForm()
    return render(request, "crear_arma.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def editar_arma(request, arma_id):
    arma = get_object_or_404(Arma, id=arma_id)
    if request.method == "POST":
        form = ArmaForm(request.POST, request.FILES, instance=arma)
        if form.is_valid():
            form.save()
            messages.success(request, "Arma actualizada correctamente.")
            return redirect("armas")
    else:
        form = ArmaForm(instance=arma)
    return render(request, "editar_arma.html", {"form": form, "arma": arma})


@user_passes_test(lambda u: u.is_staff)
def eliminar_arma(request, arma_id):
    arma = get_object_or_404(Arma, id=arma_id)
    arma.delete()
    messages.success(request, "Arma eliminada correctamente.")
    return redirect("armas")

def recuperarcontra(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            user.set_password('TemporalPass777')
            user.save()
            messages.success(request, f"Envío de email simulado. Su nueva contraseña es: TemporalPass777")
            return redirect('inicio_sesion_wiki')
        except User.DoesNotExist:
            messages.error(request, "No se encontró un usuario con ese correo.")
            return redirect('recuperarcontra')
    return render(request, "recuperarcontra.html")

def obtener_consejo():
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout=3)
        data = response.json()
        return data.get("slip", {}).get("advice", "Consejo no disponible.")
    except:
        return "Consejo no disponible."
