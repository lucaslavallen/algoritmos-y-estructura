#! estructurad de datos varibales, array, list, tuples, dic, class
import os
os.system('cls')
# listas_num = [0] * 5
lista_num = []
lista_num.append(1)
lista_num[0] = 3
lista_num.append(10) # agrega al final de la lista 
lista_num.append(5)
lista_num.insert(1,4) # elegis la posiscion donde se ubica 
lista_num.insert(7,10)

#print(lista_num)
#print(lista_num.pop()) # si esta vacion elimina el ultimo y el index permite elegir cual numero eliminar
#print(lista_num)
# print(lista_num.remove(5)) # elimina numero seleccionado
#print(lista_num.sort()) # (reverse =True) => ordana de forma inversa


#tupla_num = (1,2) # la tupla es como una constante que no se puede modificar


# def mi_funcion_prueba(lista):
#     lista.append(1)
#     lista[0] = 49


lista_test = [1,7,2,33,99] 
# mi_funcion_prueba(lista_test)
# print(lista_test)
#! [49,2,3,1] => consola

# print(len(lista_test))

# for i in range(len(lista_test)):
#     print('valor', lista_test[i])


for numero in lista_test:
    print(numero)

# Diccionarios
    
dic = {'1': 'hola', '2':'chau', '0':'chau'} #! key -> value 

dic['3'] = 49

print(dic['1'])

print(dic.get('0'))

#print(dic.keys()) # devulve una lista con todas las keys

print(dic.items()) # devulve una lista de conjunto valor 

#print(dic.pop()) #elemina un elemento

dic.update({'1': 526}) # modificar el diccionario


for key, value in dic.items():
    print(key, value)


#! Modulos  -> librerias
    
from mi_libreria import suma, resta # importa el modulo necesario
import mi_libreria as ml # cambia el nombre 

print(resta(1, 2))

print(suma(1, 1))

print(ml.multiplicar(3, 3))

from math import factorial

print(factorial(5))