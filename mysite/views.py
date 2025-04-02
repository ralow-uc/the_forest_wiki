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
  animales_data = [
      {
          'nombre': 'Murciélago',
          'imagen': 'img/Animales/1.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Realmente no se puede interactuar con ellos y solo sirven para propósitos de inmersión. Es posible matar murciélagos golpeándolos con el arma que elijas, pero no dejan caer nada.'
      },
      {
          'nombre': 'Aves',
          'imagen': 'img/Animales/2.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest. Proporcionan plumas, que son cruciales para fabricar flechas, y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales.'
      },
      {
          'nombre': 'Ciervo',
          'imagen': 'img/Animales/3.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Los ciervos se pueden encontrar en las zonas boscosas, aunque también en campos abiertos, como las Tierras Fértiles. Cuando los matan, pueden ser desollados por una piel de ciervo, luego sacrificados por cuatro carnes y finalmente dejar caer una cabeza de ciervo.'
      },
      {
          'nombre': 'Peces',
          'imagen': 'img/Animales/4.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Los peces son un grupo de animales pasivos que se pueden encontrar en el océano, río, estanques o en el agua de cuevas. Cuando se matan, los peces caen como un artículo de colección, el pescado crudo, que luego se puede cocinar o colgar en una rejilla de secado.'
      },
      {
          'nombre': 'Gansos',
          'imagen': 'img/Animales/5.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'El ganso es un animal volador y emplumado que se encuentra cerca de los lagos. Es el único pájaro que se posa en el agua, y el mismo nombre del lago de los gansos, al suroeste de Sinkhole.'
      },
      {
          'nombre': 'Lagarto',
          'imagen': 'img/Animales/6.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Las lagartijas se pueden encontrar en casi toda la superficie de la península, excepto en las costas y las regiones nevadas profundas. Cuando muere, el jugador puede obtener una piel de lagarto y un lagarto crudo, así como una cabeza de lagarto.'
      },
      {
          'nombre': 'Conejo',
          'imagen': 'img/Animales/8.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'El conejo se puede recolectar para obtener una piel de conejo, una carne de conejo cruda y una cabeza de conejo. La carne cosechada se puede cocinar al fuego o secar en una rejilla de secado y comer.'
      },
      {
          'nombre': 'Mapache',
          'imagen': 'img/Animales/9.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Los mapaches son algunos de los animales más raros del juego. Cuando los matan y los despellejan, dejan caer 2 carnes, 1 piel de mapache y 1 cabeza de mapache. A diferencia de la mayoría de los animales pequeños en The Forest, los mapaches solo se pueden matar con dos golpes de cualquier arma.'
      },
      {
          'nombre': 'Gaviota',
          'imagen': 'img/Animales/10.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest. Proporcionan plumas, que son cruciales para fabricar flechas, y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales.'
      },
      {
          'nombre': 'Ardilla',
          'imagen': 'img/Animales/11.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Las ardillas le dan al jugador una carne pequeña y una cabeza de ardilla. Al igual que con la mayoría de los animales pequeños, las ardillas se pueden matar con un solo golpe de cualquier arma en el juego.'
      },
      {
          'nombre': 'Tortuga de tierra',
          'imagen': 'img/Animales/12.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Las tortugas son animales pasivos que desovan en áreas específicas alrededor del agua, especialmente en las tierras pantanosas. Se mueven muy lentamente y se esconderán dentro de su caparazón si intentas atacarlos. Al morir, dejan caer un caparazón de tortuga y dos piezas de carne.'
      },
      {
          'nombre': 'Tortuga de mar',
          'imagen': 'img/Animales/13.png',
          'hostilidad': 'Pasivo',
          'descripcion': 'Dejan caer un caparazón de tortuga, que se puede usar para fabricar el colector de agua, o como un trineo, y dos carnes, que se pueden cocinar o secar y comer.'
      },
      {
          'nombre': 'Jabalí',
          'imagen': 'img/Animales/Boar.webp',
          'hostilidad': 'Agresivo',
          'descripcion': 'Similar al cocodrilo, el jabalí es un animal agresivo capaz de atacar y dañar al jugador. Si el jugador permanece cerca de un jabalí durante demasiado tiempo, emitirá un chillido y comenzará a cargar hacia el jugador. Si el jabalí golpea al jugador con su carga, inflige 15 puntos de daño. Al morir, suelta 2 de carne y piel.'
      },
      {
          'nombre': 'Tiburón',
          'imagen': 'img/Animales/Shark.webp',
          'hostilidad': 'Agresivo',
          'descripcion': 'Los tiburones son animales hostiles que se pueden encontrar nadando en áreas profundas del océano. Si el jugador se acerca demasiado, un tiburón lo atacará mordiéndolo. Al morir, sueltan 1 de carne y la cabeza.'
      },
      {
          'nombre': 'Cocodrilo',
          'imagen': 'img/Animales/Crocodile.webp',
          'hostilidad': 'Agresivo',
          'descripcion': 'Los cocodrilos se pueden encontrar en la parte norte del río que atraviesa la península. Al morir, dejan caer 4 pieles de lagarto, 4 carnes y su cabeza como decoración.'
      }
  ]

  return render(request, 'Animales.html', {'animales': animales_data})

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

def forowiki(request):
  return render(request, 'forowiki.html')

def registrasewiki(request):
  return render(request, 'registrase_wiki.html')

def inicio_sesion_wiki(request):
  return render(request, 'inicio_sesion_wiki.html')

def micuentatf(request):
  return render(request, 'micuentatf.html')


