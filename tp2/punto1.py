 # Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
 # criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
 # siguiente situación:

# a) cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# import heapq

# prioridad = []
# heapq.heapify(prioridad)

# cantidad = int(input("Ingrese la cantidad de elementos a imprimir: "))

# for i in range(cantidad):
#     categoria = input("Ingrese a qué categoría pertenece el documento (empleado/TI/gerente): ")
#     if categoria == "empleado":
#         indice = 1
#     elif categoria == "TI":
#         indice = 2
#     elif categoria == "gerente":
#         indice = 3
#     else:
#         print("Ha ingresado incorrectamente el nombre de la categoría.")
#         continue

#     documento = input("Ingrese el nombre del documento: ")
#     heapq.heappush(prioridad, (indice, documento))

# print("Cola de impresión:")
# while prioridad:
#     categoria, documento = heapq.heappop(prioridad)
#     # print(f"Categoría: {'empleado' if categoria == 1 else 'TI' if categoria == 2 else 'gerente'}, Documento: {documento}")
#     print (prioridad)

import queue

cola_prioridad = queue.PriorityQueue()

cantidad = int(input("Ingrese la cantidad de elementos a imprimir: "))

for i in range(cantidad):
    categoria = input("Ingrese a qué categoría pertenece el documento (empleado/TI/gerente): ")
    if categoria == "empleado":
        indice = 1
    elif categoria == "TI":
        indice = 2
    elif categoria == "gerente":
        indice = 3
    else:
        print("Ha ingresado incorrectamente el nombre de la categoría.")

   
    documento = input("Ingrese el nombre del documento: ")
    cola_prioridad.put((indice, documento))

print("Cola de impresión:")
while not cola_prioridad.empty():
    categoria, documento = cola_prioridad.get()
    print(f"Categoría: {'empleado' if categoria == 1 else 'TI' if categoria == 2 else 'gerente'}, Documento: {documento}")