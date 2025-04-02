from django.shortcuts import render

# Create your views here.
def home(request):
  cards = [
    {'title': 'Animales', 'image': 'img/img_wiki/animal2.png', 'url': 'animales'},
    {'title': 'Mapa', 'image': 'img/img_wiki/mapaforest1.png', 'url': 'lugarestf'},
    {'title': 'Enemigos', 'image': 'img/img_wiki/enemigosforest1.png', 'url': 'enemigos'},
    {'title': 'Construcciones', 'image': 'img/img_wiki/buildings.png', 'url': 'construcciones'},
    {'title': 'Plantas', 'image': 'img/img_wiki/plantaforest.png', 'url': 'flora'},
    {'title': 'Armas', 'image': 'img/img_wiki/armasthf1.png', 'url': 'armas'},
    {'title': 'Consumibles', 'image': 'img/img_wiki/consumibles.png', 'url': 'consumibles'},
    {'title': 'Historia', 'image': 'img/img_wiki/Storytf.png', 'url': 'historia'}
  ]
  return render(request, 'menuprincipal_wiki.html', {'cards': cards})

def animales(request):
  return render(request, 'Animales.html')

def lugarestf(request):
  return render(request, 'Lugarestf.html')

def enemigos(request):
  return render(request, 'Enemigos.html') 

def construcciones(request):
  return render(request, 'Construcciones.html')

def flora(request):
  return render(request, 'Flora.html')

def armas(request):
  return render(request, 'Armas.html')

def consumibles(request):
  return render(request, 'Consumibles.html')

def historia(request):
  return render(request, 'historia.html')


