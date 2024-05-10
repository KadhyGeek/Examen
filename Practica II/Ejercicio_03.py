""" Ejercicio 03"""

""" 3.
Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
-
El programa deberá tener una función para ingresar dos datos por consola.
-
Deberá tener una función en el caso haya una división entre cero mencionar el error.
-
Deberá tener una función la cuál evaluará la suma de datos incorrectos, mencionar el error
-
Deberá tener una función donde se ingresarán N datos a una lista y al momento de pedir un índice incorrecto para mostrarlo 
en consola y no exista respectivamente ese índice, aplicar try, except respectivamente.
-
Todas las funciones creadas tendrán la facultad de volver a pedir el número hasta que se ingresen correctamente.  """

var_1 = input("ingrese primer dato: ")
var_2 = input("ingrese segundo dato: ")


# Funciones de la calculadora
def suma(num1, num2):
    try:
        return num1 + num2
    except ArithmeticError:
        return "los valores de la suma de datos son incorrectos."

def listar(num1, num2):
    list = []
    list.append(num1)
    list.append(num2)
    return list
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "No se puede dividir entre cero, ingrese el numero nuevamente", exit()

# Menú principal
print("Por favor, elige una operación:")
print("1. Suma")
print("2. lista")
print("3. División")

# Solicitar al usuario que ingrese la opción
opcion = input("Ingresa una opción (1/2/3): ")

# Solicitar al usuario que ingrese los números
try:
    num1 = float(input("Ingresa el primer número: "))
except ValueError:
    print("ingrese un valor numerico")
except TypeError:
    print("Vuelva a ingresar un número")

try:
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("ingrese un valor numerico")
except TypeError:
    print("Vuelva a ingresar un número")


# Realizar la operación seleccionada
if opcion == '1':
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == '2':
    print(num1, " lista de ", num2, "elementos", listar(num1, num2))

elif opcion == '4':
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opción inválida")