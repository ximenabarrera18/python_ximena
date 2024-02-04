""" En este problema debemos de definir una constante con el valor de PI como 3,1416 y
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o
flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo
en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un
mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""
from Metodos import informacion,error,advertencia,val_float
def area_circulo():
    pi = 3.1416
    while True:
        print(informacion("Digite el radio de un círculo: "))
        radio=val_float(input())
        if radio <= 0:
            print(error("ERROR: El radio debe ser un número positivo."))
            print(advertencia("No se puede hallar el área del círculo. Intenta de nuevo."))
            continue
        else:
            area = pi * radio**2
            area_round=round(area,3)
            print(informacion(f"El área del círculo es: {area_round}"))
            break

if __name__ == "__main__":
    area_circulo()