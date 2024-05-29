class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise Exception("La pila está vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            raise Exception("La pila está vacía")

    def tamaño(self):
        return len(self.elementos)

def posicion_personajes(pila, nombres):
    posiciones = {nombre: -1 for nombre in nombres}
    pila_aux = Pila()
    posicion = 1

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'] in nombres:
            posiciones[personaje['nombre']] = posicion
        posicion += 1

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return posiciones

def personajes_mas_de_5_peliculas(pila):
    personajes = []
    pila_aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['peliculas'] > 5:
            personajes.append((personaje['nombre'], personaje['peliculas']))

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

def peliculas_viuda_negra(pila):
    cantidad_peliculas = 0
    pila_aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'] == 'Black Widow':
            cantidad_peliculas = personaje['peliculas']

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return cantidad_peliculas

def personajes_con_letras_C_D_G(pila):
    personajes = []
    pila_aux = Pila()

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        pila_aux.apilar(personaje)
        if personaje['nombre'][0] in 'CDG':
            personajes.append(personaje['nombre'])

    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())

    return personajes

# Ejemplo de uso
pila_personajes = Pila()
pila_personajes.apilar({'nombre': 'Iron Man', 'peliculas': 10})
pila_personajes.apilar({'nombre': 'Captain America', 'peliculas': 9})
pila_personajes.apilar({'nombre': 'Thor', 'peliculas': 8})
pila_personajes.apilar({'nombre': 'Black Widow', 'peliculas': 7})
pila_personajes.apilar({'nombre': 'Hulk', 'peliculas': 6})
pila_personajes.apilar({'nombre': 'Rocket Raccoon', 'peliculas': 4})
pila_personajes.apilar({'nombre': 'Groot', 'peliculas': 3})

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot
posiciones = posicion_personajes(pila_personajes, ['Rocket Raccoon', 'Groot'])
print("Posiciones de Rocket Raccoon y Groot:", posiciones)

# b. determinar los personajes que participaron en más de 5 películas
personajes_mas_5 = personajes_mas_de_5_peliculas(pila_personajes)
print("Personajes con más de 5 películas:", personajes_mas_5)

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow)
peliculas_black_widow = peliculas_viuda_negra(pila_personajes)
print("Películas de Black Widow:", peliculas_black_widow)

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
personajes_letras_CDG = personajes_con_letras_C_D_G(pila_personajes)
print("Personajes cuyos nombres empiezan con C, D o G:", personajes_letras_CDG)
