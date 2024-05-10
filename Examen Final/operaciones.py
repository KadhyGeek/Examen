import math
import random


def listaAleatorios():
    n = int(input("Ingrese cuantos numeros aleatorios desea obtener: "))
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(0, 1000)
    return lista


def raiz_quadrado(x):
    return math.sqrt(x)
