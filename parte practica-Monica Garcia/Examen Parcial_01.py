
"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre, apellido y edad de un usuario. Mostrar en consola el
nombre completo del trabajador
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""



nombre = input("Ingrese el nombre del usuario: ")

apellido = input("Ingrese el apellido del usuario: ")

edad = int(input("Ingrese la edad del usuario: "))

nombre_completo = nombre + " " + apellido

print(nombre_completo)

print("El nombre del usuario es {} y su tipo de dato es ".format(nombre),type(nombre))
print("El apellido del usuario es {} y su tipo de dato es ".format(apellido),type(apellido))
print("La edad del usuario es {} y su tipo de dato es ".format(edad),type(edad))


lista_emp = [input("Ingrese el nombre del primer trabajador: "), int(input("Ingrese la edad del primer trabajador: ")), input("Ingrese el nombre del segundo trabajador: "), int(input("Ingrese la edad del segundo trabajador: "))]

nombre_trabajador1, edad_trabajador1, nombre_trabajador2 , edad_trabajador2 = lista_emp

suma = lista_emp[1] + lista_emp[3]

print("la suma de las edades de los trabajadores es {}".format(suma))

