"""Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y
seis"""

from Metodos import error,informacion

def numero_palabras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 0 <= numero <= 99:
        if numero < 10:
            print(f"{unidades[numero]}")
        elif 10 <= numero < 20:
            print(f"{unidades[numero % 10]} y {decenas[1]}")
        else:
            if numero % 10 == 0:
                print(informacion(f"{decenas[numero // 10]}"))
            else:
                print(informacion(f"{decenas[numero // 10]} y {unidades[numero % 10]}"))
    else:
        print(error("Por favor, ingresa un número entre 0 y 99."))

# Solicitar la informacion al usuario 
while True:
    try:
        numero_ingresado = int(input("Ingresa un número entre 0 y 99: "))
        break  

# Si la entrada es válida puede salir 
    except ValueError:
        print(error("ERROR, ingresa un número entero válido."))

# Llamar a la función
numero_palabras(numero_ingresado)
