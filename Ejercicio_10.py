"""Dado un número (leído por teclado), que representa los segundos que ha invertido una
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido.
Imprima el resultado por pantalla."""

from Metodos import error,informacion

def convertir_segundos_a_tiempo(segundos):
    if segundos < 0:
        print("Por favor, ingresa un número no negativo.")
    else:
        # Calcular horas, minutos y segundos
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos_restantes = segundos % 60
        
        # Mostrar resultados
        print("")
        print(informacion(f"Tiempo calculado :"))
        print(informacion(f"{horas} horas"))
        print(informacion(f"{minutos} minutos"))
        print(informacion(f"{segundos_restantes} segundos"))

# Solicitar input al usuario con validación
while True:
    try:
        segundos_ingresados = int(input("Ingresa el número de segundos a calcular: "))
        break  # Si la entrada es válida, salir del bucle
    except ValueError:
        print(error("ERROR, ingresa un número entero válido."))

# Llamar a la función con los segundos ingresados
convertir_segundos_a_tiempo(segundos_ingresados)

