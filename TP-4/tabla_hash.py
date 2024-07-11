def hash_tipo_pokemon(valor):
    return valor

def hash_ultimo_digito(numero):
    return str(numero)[-1:]  

def nivel_hash(nivel):
    return nivel // 10        

def cargar_pokemon(tabla_tipos, tabla_ultimo_digito, tabla_nivel, pokemon):
    tipo_hash = hash_tipo_pokemon(pokemon['tipo'])  # Corregido para obtener el tipo del Pokemon
    ultimo_digito_hash = hash_ultimo_digito(pokemon['numero'])  # Corregido para obtener el número del Pokemon
    nivel_hash_value = nivel_hash(pokemon['nivel'])  # Corregido para obtener el nivel del Pokemon
    
    if tipo_hash not in tabla_tipos:
        tabla_tipos[tipo_hash] = []
    tabla_tipos[tipo_hash].append(pokemon)
    
    if ultimo_digito_hash not in tabla_ultimo_digito:
        tabla_ultimo_digito[ultimo_digito_hash] = []
    tabla_ultimo_digito[ultimo_digito_hash].append(pokemon)
    
    if nivel_hash_value not in tabla_nivel:
        tabla_nivel[nivel_hash_value] = []
    tabla_nivel[nivel_hash_value].append(pokemon)

def mostrar_pokemon_por_ultimo_digito(tabla, digitos):
    for digito in digitos:
        if digito in tabla:
            print(f"Pokémons cuyo número termina en {digito}:")
            for pokemon in tabla[digito]:
                print(pokemon['nombre'])
        else:
            print(f"No hay Pokémons cuyo número termine en {digito}")

def mostrar_pokemon_por_nivel(tabla, niveles):
    for nivel in niveles:
        if nivel in tabla:
            print(f"Pokémons cuyo nivel es múltiplo de {nivel * 10}:")
            for pokemon in tabla[nivel]:
                print(pokemon['nombre'])
        else:
            print(f"No hay Pokémons cuyo nivel sea múltiplo de {nivel * 10}")

def mostrar_pokemon_por_tipo(tabla, tipos):
    print("Pokémons de los siguientes tipos:")
    for tipo in tipos:
        if tipo in tabla:
            for pokemon in tabla[tipo]:
                print(pokemon['nombre'])
        else:
            print(f"No hay Pokémons del tipo {tipo}")
            
pokemons = [
    {'numero': 25, 'nombre': 'Pikachu', 'tipo': 'Electrico', 'nivel': 15},
    {'numero': 133, 'nombre': 'Eevee', 'tipo': 'Normal', 'nivel': 20},
    {'numero': 442, 'nombre': 'Spiritomb', 'tipo': 'Fantasma', 'nivel': 30},  # Aquí se elige un tipo principal
    # Añade más pokemons si es necesario
]

tabla_tipos = {}
tabla_ultimo_digito = {}
tabla_nivel = {}

# Cargar los Pokémons en las tablas hash
for pokemon in pokemons:
    cargar_pokemon(tabla_tipos, tabla_ultimo_digito, tabla_nivel, pokemon)

# Mostrar los Pokémons según los requisitos
mostrar_pokemon_por_ultimo_digito(tabla_ultimo_digito, [3, 7, 9])
mostrar_pokemon_por_nivel(tabla_nivel, [2, 5, 10])
mostrar_pokemon_por_tipo(tabla_tipos, ['Acero', 'Fuego', 'Electrico', 'Hielo'])