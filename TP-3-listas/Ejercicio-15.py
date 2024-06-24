
from Lista_enlazada import show_list_list, search
from random import randint

pokemones = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }
]

entrenadores = [
    {
        "nombre": "Ash",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

lista= []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista.append(entrenador)

for pokemon in pokemones:
    pos=randint(0, len(lista)-1)
    lista[pos]['sublist'].append(pokemon)


# a. obtener la cantidad de Pokémons de un determinado entrenador;
def pokemon_entrenador (lista):
    entrenador=input("Ingrese el nombre del entrenador del que quiere conocer su cantidad de pokemons: ")
    pos= search(lista, 'nombre', entrenador)
    if pos is not None:
        cantidad = lista[pos]['sublist']
        print(f"El entrenador tiene {len(cantidad)} pokemons")

# b. listar los entrenadores que hayan ganado más de tres torneos;
def tres_torneos (lista):
    tres=[]
    for entrenador in lista:
        if entrenador['torneos_ganados']>3:
            tres.append(entrenador)
    show_list_list("Los entrenadores que ganaron mas de tres torneos son: ", "Sus pokemons son: ", tres)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def torneos_nivel (lista):
    torneos = 0
    nivel = 0
    for entrenador in lista:
        if entrenador['torneos_ganados']>torneos:
            torneos = entrenador['torneos_ganados']
            ent_torneos = entrenador
    pokemons= ent_torneos['sublist']
    for pokemon in pokemons:
        if pokemon['nivel']>nivel:
            nivel = pokemon['nivel']
            pok_nivel=pokemon
    print(f"El entrenador con mas torneos ganados es {ent_torneos['nombre']} y su pokemon de mayor nivel es {pok_nivel['nombre']}")
    
# d. mostrar todos los datos de un entrenador y sus Pokémos;
def barrido (lista):
    show_list_list("Los entrenadores son: ", "Sus pokemons son: ", lista)

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def mas_79 (lista):
    print("Los entrenadores cuyo porcentaje de batallas ganados es mayor al 79% son:")
    for entrenador in lista:
        batallas_total= entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']
        porc= entrenador['batallas_ganadas'] * 100 / batallas_total
        if porc>79:
            print(entrenador['nombre'])

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def tipo_subtipo(lista):
    for entrenador in lista:
        for pokemon in entrenador['sublist']:
            if pokemon['tipo'] == "fuego" and pokemon['subtipo'] == "planta":
                print(f"{entrenador['nombre']} tiene {pokemon['nombre']} de tipo fuego y planta")
            elif pokemon['tipo'] == "agua" and pokemon['subtipo'] == "volador":
                print(f"{entrenador['nombre']} tiene {pokemon['nombre']} de tipo agua y volador")    

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def prom_nivel(lista):
    entrenador=input("Ingrese el nombre del entrenador que busca: ")            
    pos= search(lista, 'nombre', entrenador)
    nivel=0
    p=0
    for pokemon in lista[pos]['sublist']:
        nivel += pokemon['nivel']
        p+=1
    print(f"El promedio de nivel de los Pokémons de {entrenador} es {nivel/p}")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def entrenadores_pok (lista):
    pok=input("Ingrese el nombre del pokemon buscado: ")
    e=0
    for entrenador in lista:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre']==pok:
                e+=1
    print(f"{e} entrenadores tienen a {pok}")

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def repetidos (lista):
    rep={}
    for entrenador in lista:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] in rep:
                rep[pokemon['nombre']].append(entrenador['nombre'])
            else:
                rep[pokemon['nombre']]=[entrenador['nombre']]
    for pok, ent in rep.items():
        print(pok, ent)
        if len(ent)>1:
            print(f"Los entrenadores {ent} tienen a {pok}")

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: 
# Tyrantrum, Terrakion o Wingull;
def tyrantrum_terrakion_wingull (lista):
    for entrenador in lista:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre']=="Tyrantrum" or pokemon['nombre']=="Terrakion" or pokemon['nombre']=="Wingull":
                print(f"{entrenador['nombre']} tiene a {pokemon['nombre']}")

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
def pok_ent (lista):
    entrenador=input("Ingrese el nombre del entrenador: ")
    pok=input("Ingrese el nombre del pokemon: ")
    pos= search(lista, 'nombre', entrenador)
    for pokemon in lista[pos]['sublist']:
        if pokemon['nombre']==pok:
            print(f"{entrenador} tiene a {pok}")

pokemon_entrenador(lista)
tres_torneos(lista)
torneos_nivel(lista)
barrido(lista)
mas_79(lista)
tipo_subtipo(lista)
prom_nivel(lista)
entrenadores_pok(lista)
repetidos(lista)
tyrantrum_terrakion_wingull(lista)
pok_ent(lista)