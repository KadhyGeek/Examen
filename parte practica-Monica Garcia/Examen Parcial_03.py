"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario y aumentar en 10 solo la edad
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

var_1 = {}

var_1["nombre"] = input("ingrese un nombre: ")
var_1["Apellido"] = input("ingrese un apellido: ")
var_1["edad"] = int(input("ingrese una edad: "))
var_1["dni"] = input("ingrese un dni: ")

print(f"El diccionario es: {var_1}")

var_1["edad"] = var_1["edad"] + 10

var_1["profesion"] = input("ingrese una profesión: ")

del var_1["dni"]

print("El nuevo diccionario es: {}". format(var_1))