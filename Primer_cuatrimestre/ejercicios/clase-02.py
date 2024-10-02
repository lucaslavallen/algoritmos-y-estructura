# Clases y Objetos
import os
os.system('cls')
class car: 
    model, color, id = None, None, None
    
    def funcion_car(self):
        print("prueba funcion")
    
    def __str__(self): #meodo que se va llamar cuando haga 
        return f'car data {self.model} {self.color} {self.id}'
    

car_1 = car()
car_1.color = 'red'
car_1.model = '1998'

print(car_1.model, car_1.color)
print(car_1)


#!  Revision de string 

cadena = 'hola mondo'

print(cadena.capitalize()) # acomoda la cadena pone mayuscula al princpio
print(cadena.count('o'))
print(cadena.find('th')) # te encuentra la palabra  te devulve un valor
print(cadena.lower())
print(cadena.upper())
print(cadena.replace('munDo', 'world'))
print(cadena.strip()) #sirve para quitar espacioss en blancos 
print(cadena.split(' ')) # se parar caracteres en un criterio util

palabras = ['una', 'chau', 'nuevo']

nueva_cadena = '_'.join(palabras) # join sirve para juntar un conjunto de plabras 

print(nueva_cadena)


if 'j' == 'J':
    print('on las misma letra')
else:
    print('no son la misma letra')

names = ['Juan', 'Julian', 'Maria', 'Ana', 'Julieta']


for name in names:
    if name.startswith("J"):
        print(name)

    



