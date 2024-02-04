""" Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes."""

from Metodos import informacion,val_numero

def comparacion_numeros(num1, num2, num3):

    # Para hallar el numero mayor 
    mayor = max(num1, num2, num3)
    
    # para hallar el numero menor 
    menor = min(num1, num2, num3)

    # para hallar el numero medio 
    medio = num1 + num2+ num3- mayor - menor
    
    # Mostrar los resultados
    print(informacion(f"El mayor es: {mayor}"))
    print(informacion(f"El menor es: {menor}"))
    print(informacion(f"el medio es:{medio}"))

# Solicitar la informacion al usuario 
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

# Llamar a la función con los valores ingresados
if __name__== "__main__":
    comparacion_numeros(num1,num2,num3)
