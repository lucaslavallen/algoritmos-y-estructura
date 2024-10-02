def obtener_personaje_superheroe(super_heroes, superheroe):
    for personaje in super_heroes:
        if personaje['nombre'] == superheroe:
            return personaje['biografia']
    return "Superhéroe no encontrado"

def super_heroes_femeninos(super_heroes):
    return [personaje['nombre'] for personaje in super_heroes if personaje['nombre'].lower() in ['capitana marvel', 'black widow', 'la mujer invisible']]

c. Mostrar los nombres de los personajes masculinos
def personajes_masculinos(super_heroes):
    return [personaje['nombre'] for personaje in super_heroes if personaje['nombre'].lower() not in ['capitana marvel', 'black widow', 'la mujer invisible']]

def obtener_superheroe_de_personaje(super_heroes, personaje):
    for heroe in super_heroes:
        if personaje in heroe['biografia']:
            return heroe['nombre']
    return "Personaje no encontrado"


def obtener_personajes_por_letra(super_heroes, letra):
    return [personaje for personaje in super_heroes if personaje['nombre'].startswith(letra)]

def encontrar_carol_danvers(super_heroes):
    for personaje in super_heroes:
        if "Carol Danvers" in personaje['biografia']:
            return personaje['nombre']
    return "Carol Danvers no está en la lista"

print("Biografía de Capitana Marvel:", obtener_personaje_superheroe(super_heroes, "Capitana Marvel"))
print("Superhéroes femeninos:", super_heroes_femeninos(super_heroes))
print()
print("Personajes masculinos:", personajes_masculinos(super_heroes))
print()
print("Superhéroe de Scott Lang:", obtener_superheroe_de_personaje(super_heroes, "Scott Lang"))
print()
print("Personajes cuyos nombres comienzan con S:", obtener_personajes_por_letra(super_heroes, "S"))
print()
print("Nombre de superhéroe de Carol Danvers:", encontrar_carol_danvers(super_heroes))