"""Ejercicio 01"""
import random

"""1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (3 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola."""


def lista():
    list = [0] * 10
    for i in range(10):
        list[i] = int(random.randint(0, 1000))
    return list


def imprimir_unicas():
    lista_unicas = list(set(lista()))
    return lista_unicas


def imprimir_ordenada():
    lista_ordenada = sorted(imprimir_unicas())
    lista_maymen = list(reversed(lista_ordenada))
    lista_menmay = sorted(lista())
    return lista_maymen, lista_menmay


def imprimir_maypar():
    listar = list(imprimir_unicas())
    while max(listar) % 2 != 0:
        x = max(listar)
        listar.remove(x)
    else:
        return max(listar)


print(lista())
print(imprimir_unicas())
print(imprimir_ordenada())
print(imprimir_maypar())
