"""Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
"""
from Metodos import informacion,error

def mostrar_digitos_en_inverso(numero):

    # Convertir el número a una cadena para facilitar la manipulación de dígitos
    val_num = str(numero)
    
    # Mostrar los dígitos en orden inverso
    print(informacion("Dígitos de manera ordenada:"))
    for digito in reversed(val_num):
        print(informacion(digito))

# Solicitar input al usuario con validación
while True:
    try:
        numero_ingresado = int(input("Ingresa el numero: "))
        print("")
        break 
 # Si la entrada es válida, salir del bucle
    except ValueError:
        print(error("ERROR, ingresa un número válido."))

# Llamar a la funcion 
mostrar_digitos_en_inverso(numero_ingresado)
