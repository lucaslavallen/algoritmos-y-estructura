def usar_la_fuerza(mochila, posicion=0, objetos_sacados=0):
    if posicion == len(mochila):
        return "No se encontró un sable de luz en la mochila", objetos_sacados
    elif mochila[posicion] == "sable de luz":
        return "Se encontró un sable de luz en la posición", posicion, "después de sacar", objetos_sacados, "objetos"
    else:
        return usar_la_fuerza(mochila, posicion + 1, objetos_sacados + 1)

mochila_jedi = ["botas", "comida", "sable de luz", "brújula"]
resultado = usar_la_fuerza(mochila_jedi)
print(resultado)