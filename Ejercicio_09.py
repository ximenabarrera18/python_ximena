""" Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe
de imprimir el mes correspondiente en texto"""

from Metodos import informacion, error

def obtener_mes_texto(numero_mes):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    if 1 <= numero_mes <= 12:
        mes_texto = meses[numero_mes - 1]
        print(informacion(f"El número {numero_mes} corresponde al mes de {mes_texto}."))
    else:
        print(error ("ERROR,ingresa un número entre 1 y 12."))

# Solicitar input al usuario
numero_ingresado = int(input("Ingresa un número entre 1 y 12: "))

# Llamar a la función con el número ingresado
if __name__=="__main__":
    obtener_mes_texto(numero_ingresado)
