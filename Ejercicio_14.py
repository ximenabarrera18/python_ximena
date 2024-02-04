"""Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma"""

from Metodos import informacion

def palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para hacer la comparación
    cadena = cadena.replace(" ", "").lower()
    
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Solicitar la cadena al usuario con validación
cadena_input = input("Ingresa una cadena de caracteres: ")

# Validar que la cadena no esté vacía
while not cadena_input:
    cadena_input = input("Por favor, ingresa una cadena de caracteres: ")

# Verificar si es un palíndromo
if palindromo(cadena_input):
    print(informacion("La cadena es un palíndromo."))
else:
    print(informacion("La cadena no es un palíndromo."))
