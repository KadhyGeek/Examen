""" Ejercicio 01"""
from datetime import datetime

""" 1.
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
-
Crear una clase llamada Persona donde sus atributos deben ser nombre, edad, saldo y de nacionalidad peruana 
(use el manejo de errores para el tipo de dato) y un método para solicitar su nombre y edad.
-
Tendrá un método cumpleaños donde cada vez que invoque aumentará en un año la edad de la persona.
-
Crear la instancia de la clase Persona y usar su método cumpleaños para incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por pantalla dicha edad actualizada).
-
Crear una función que retorne solamente la fecha, hora y minuto que se ha registrado esta persona (Mostrar por pantalla este valor)"""

class Persona:
    nacionalidad = "Peruana"
    def __init__(self):

            try:
                    self.nombre =str(input("Ingrese el nombre: "))
            except ValueError:
                    print("Por favor ingrese un nombre")
                    exit()

            try:
                    self.edad = int(input("Ingrese el edad: "))
            except TypeError:
                    print("Por favor ingrese un valor numérico")
                    exit()

            try:
                    self.saldo =input("Ingrese el saldo: ")
            except TypeError:
                    print("Por favor ingrese un valor numérico")
                    exit()

    def cumpleanos(self):

        self.edad +=  1
        return self.edad

    def registro(self):
        self.fecha = datetime.now()
        return self.fecha.date(), self.fecha.hour, self.fecha.minute



person = Persona()
print(person.cumpleanos())
print(person.cumpleanos())
print(person.registro())

