class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def encolar(self, dato):
        nodo = Nodo(dato)
        if self.final:
            self.final.siguiente = nodo
        self.final = nodo
        if not self.frente:
            self.frente = nodo
        self.tamaño += 1

    def desencolar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        self.tamaño -= 1
        return dato

    def esta_vacia(self):
        return self.frente is None

    def ver_frente(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.frente.dato

    def __len__(self):
        return self.tamaño


def nombre_personaje_superheroe(cola, nombre_superheroe):
    nombre_personaje = None
    cola_aux = Cola()

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['superheroe'] == nombre_superheroe:
            nombre_personaje = personaje['nombre']

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return nombre_personaje


def nombres_superheroes_femeninos(cola):
    nombres_femeninos = []
    cola_aux = Cola()

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['genero'] == 'F':
            nombres_femeninos.append(personaje['superheroe'])

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return nombres_femeninos


def nombres_personajes_masculinos(cola):
    nombres_masculinos = []
    cola_aux = Cola()

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['genero'] == 'M':
            nombres_masculinos.append(personaje['nombre'])

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return nombres_masculinos


def nombre_superheroe_personaje(cola, nombre_personaje):
    nombre_superheroe = None
    cola_aux = Cola()

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['nombre'] == nombre_personaje:
            nombre_superheroe = personaje['superheroe']

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return nombre_superheroe


def datos_personajes_con_letra_S(cola):
    personajes_S = []
    cola_aux = Cola()

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['nombre'].startswith('S') or personaje['superheroe'].startswith('S'):
            personajes_S.append(personaje)

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return personajes_S


def encontrar_personaje(cola, nombre_personaje):
    nombre_superheroe = None
    cola_aux = Cola()
    encontrado = False

    while not cola.esta_vacia():
        personaje = cola.desencolar()
        cola_aux.encolar(personaje)
        if personaje['nombre'] == nombre_personaje:
            nombre_superheroe = personaje['superheroe']
            encontrado = True

    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())

    return encontrado, nombre_superheroe


# Ejemplo de uso
cola_personajes = Cola()
cola_personajes.encolar({'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
cola_personajes.encolar({'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
cola_personajes.encolar({'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
cola_personajes.encolar({'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
cola_personajes.encolar({'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_personaje = nombre_personaje_superheroe(cola_personajes, 'Capitana Marvel')
print("Nombre del personaje de Capitana Marvel:", nombre_personaje)

# b. mostrar los nombres de los superhéroes femeninos
superheroes_femeninos = nombres_superheroes_femeninos(cola_personajes)
print("Superhéroes femeninos:", superheroes_femeninos)

# c. mostrar los nombres de los personajes masculinos
personajes_masculinos = nombres_personajes_masculinos(cola_personajes)
print("Personajes masculinos:", personajes_masculinos)

# d. determinar el nombre del superhéroe del personaje Scott Lang
nombre_superheroe = nombre_superheroe_personaje(cola_personajes, 'Scott Lang')
print("Nombre del superhéroe de Scott Lang:", nombre_superheroe)

# e. mostrar todos datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
personajes_letra_S = datos_personajes_con_letra_S(cola_personajes)
print("Personajes o superhéroes cuyos nombres comienzan con S:", personajes_letra_S)

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes
encontrado, superheroe_carol = encontrar_personaje(cola_personajes, 'Carol Danvers')
print("Carol Danvers encontrado:", encontrado, "Nombre de superhéroe:", superheroe_carol)
