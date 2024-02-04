"""Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot"""

from Metodos import informacion
def catetos():
    cateto1 = float(input("Ingrese el valor del cateto UNO: "))
    cateto2 = float(input("Ingrese el valor del cateto DOS: "))
    return cateto1, cateto2

def calcular_hipotenusa(cateto1, cateto2):
    return (cateto1*2 + cateto2)*0.5

def mostrar_resultado(hipotenusa):
    print(informacion(f"La hipotenusa del triángulo es: {hipotenusa}"))

cateto1, cateto2 = catetos()

hipotenusa = calcular_hipotenusa(cateto1, cateto2)

if __name__== "main_":
    mostrar_resultado(hipotenusa)