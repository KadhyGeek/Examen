""" Ejercicio 02"""
from datetime import datetime

""" 2.
Usando el concepto de herencia y encapsulación (para saldo) para crear el siguiente programa (3 ptos):
Reglas:
-
Agregar un atributo saldo a la clase persona (ejercicio anterior).
-
Crear un método transferencia y mostrar saldo (mostrará el saldo actual que tiene la persona) para la clase mencionada
-
El método transferencia hace que la Persona que llame al método pueda transferir la cantidad monto al objeto Persona2 por consiguiente deberá ir actualizando 
también el saldo o monto que tiene la otra persona en su cuenta cada vez que use el método transferencia
-
Comprobar si no se tiene dinero suficiente no se ejecuta la acción e imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo menos realizando 
una transferencia y con dos personas. """

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

            self.__saldo = 0

    def cumpleanos(self):

        self.edad +=  1
        return self.edad

    def registro(self):
        self.fecha = datetime.now()
        return self.fecha.date(), self.fecha.hour, self.fecha.minute

    def transferencia(self):
        self.__saldo += 100

    def cuenta(self):
        return self.__saldo

class Empleado(Persona):
    def __init__(self):
        self.__saldo = 0

    def transferencia(self):
        self.__saldo += 100

    def retiro(self):
        self.__saldo -= 50
        if self.__saldo < 0:
            self.__saldo = self.__saldo

    def cuenta(self):
        if self.__saldo < 0:
            return "Saldo insuficiente"
        else:
            return self.__saldo


empleado = Empleado()

empleado.transferencia()
empleado.cuenta()
print(empleado.cuenta())
print(empleado.registro())
print(empleado.transferencia())
print(empleado.cuenta())
print(empleado.cuenta())
print(empleado.transferencia())
print(empleado.transferencia())
print(empleado.transferencia())
print(empleado.cuenta())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.retiro())
print(empleado.cuenta())

