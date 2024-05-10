""" 2.Usando el concepto y funciones de listas, realizar un programa con
las siguientes características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas. """
import random

lista_1= []

for i in range(10):
    lista_1.append(random.randint(2,50))
print(lista_1)

lista_cubos = []
for i in lista_1:
    lista_cubos.append(pow(i,3))
print(lista_cubos)

lista_cuadrados = []

for i in lista_1:
    lista_cuadrados.append(pow(i,2))
print(lista_cuadrados)

nueva_lista = lista_cuadrados + lista_cubos
print("La lista actual es: {}".format(nueva_lista))
nueva_lista.reverse()
print("La lista invertida es: {}".format(nueva_lista))