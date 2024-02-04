"""Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres."""

from Metodos import informacion

def contar_ocurrencias(caracter, cadena):

    # Inicializar 
    contador = 0
    
    # 
    for char in cadena:
        
        # Verificar el caracterr
        if char == caracter:
            contador += 1
    
    # Mostrar el resultado
    print(informacion(f"El carácter '{caracter}' aparece {contador} veces en la cadena."))

# Solicitar informacion al usuario
caracter_ingresado = input("Ingresa un carácter: ")
cadena_ingresada = input("Ingresa una cadena de caracteres: ")

# Llamar a la función 
contar_ocurrencias(caracter_ingresado, cadena_ingresada)
