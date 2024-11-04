def mostrar_personajes_por_planeta(jedis, planetas):
    personajes = [jedi['name'] for jedi in jedis if jedi['homeworld'] in planetas]
    return personajes

def planeta_natal(jedis, nombres):
    planetas = {jedi['name']: jedi['homeworld'] for jedi in jedis if jedi['name'] in nombres}
    return planetas

def insertar_personaje_antes_de(jedis, nuevo_personaje, nombre_referencia):
    for i, jedi in enumerate(jedis):
        if jedi['name'] == nombre_referencia:
            jedis.insert(i, nuevo_personaje)
            break
    return jedis

def eliminar_personaje_despues_de(jedis, nombre_referencia):
    for i, jedi in enumerate(jedis):
        if jedi['name'] == nombre_referencia and i + 1 < len(jedis):
            jedis.pop(i + 1)
            break
    return jedis

planetas = ["Alderaan", "Endor", "Tatooine"]
personajes_en_planetas = mostrar_personajes_por_planeta(jedis, planetas)
print("Personajes en Alderaan, Endor y Tatooine:", personajes_en_planetas)

nombres = ["Luke Skywalker", "Han Solo"]
planetas_natal = planeta_natal(jedis, nombres)
print("Planeta natal de Luke Skywalker y Han Solo:", planetas_natal)

nuevo_personaje = {
    "name": "Ahsoka Tano",
    "rank": "Jedi Knight",
    "species": "Togruta",
    "master": "Anakin Skywalker",
    "lightsaber_color": "White",
    "homeworld": "Shili",
    "birth_year": "36BBY",
    "height": 1.73,
    "to_darkside": None,
    "come_lightside": None
}
jedis_actualizados = insertar_personaje_antes_de(jedis, nuevo_personaje, "Yoda")
print("Lista actualizada con Ahsoka Tano antes de Yoda:", [jedi['name'] for jedi in jedis_actualizados])

jedis_actualizados = eliminar_personaje_despues_de(jedis, "Jar Jar Binks")
print("Lista actualizada tras eliminar personaje después de Jar Jar Binks:", [jedi['name'] for jedi in jedis_actualizados])