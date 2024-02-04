"""En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el numero ingresado por el usuario es múltiplo de 2 y 3. Sabemos
que un número es múltiplo de otro cuando al dividir estos dos números el residuo sea 0. Si el usuario ingresó
un valor negativo o cero tendremos que emitir un mensaje informando las causas por las cuales no se podrá 
efectuar la operación. 
"""
from Metodos import informacion,aviso,advertencia,val_numero
def hallar_multiplo():
    print(informacion("Verificar si es múltiplo de 2 y 3"))
    print(" ")
    while True:
        print(aviso("Digita un numero\n"))
        numero=val_numero(input())
        if numero <=0:
            print("No permitido")
            print("Digita un numero mayor a 0 por favor")
            
        elif numero % 2== 0 and numero % 3==0:
            print(informacion(f"El número {numero} es múltiplo de 2 y de 3"))
            break
        else:
            print(advertencia(f"El número {numero} no es múltiplo de 2 y de 3"))
            break
if __name__=="__main__":
    hallar_multiplo()