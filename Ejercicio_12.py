"""Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no."""

from Metodos import error,informacion

def numero_capicua(numero):
    # Convertir el número a una cadena para facilitar la manipulación de dígitos
    numero_str = str(numero)
    
    # Verificar si el número de cifras es par
    if len(numero_str) % 2 != 0:
        print(error("El número de cifras no es par."))
        return
    
    # Verificar si el número es capicúa
    if numero_str == numero_str[::-1]:
        print(informacion(f"{numero} es un número capicúa."))
    else:
        print(informacion(f"{numero} no es un número capicúa."))

# Solicitar input al usuario con validación
while True:
    try:
        numero_ingresado = int(input("Ingresa un número: "))
        break  # Si la entrada es válida, salir del bucle
    except ValueError:
        print(error("ERROR, ingresa un número entero válido."))

# Llamar a la función con el número ingresado
numero_capicua(numero_ingresado)
