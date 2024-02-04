from Metodos import informacion,val_numero,error,advertencia
import Ejercicio_01
def menu():
    while True:
        print(informacion("Seleccione un ejercicio para ejecutar"))
        print("")
        print(informacion("1. Hallar el cociente"))
        print(" ")
        print(informacion("30. Salir"))
        
        opcion =val_numero((input(informacion("Digite un número: "))))

        if opcion is None:
            print(informacion("Por favor, ingrese un número válido."))
        elif opcion == 1:
            Ejercicio_01.hallar_cociente()
        elif opcion == 30:
            print(informacion("Saliendo del programa. ¡Hasta luego!"))
            break
        else:
            print(informacion("Opción no válida. Inténtelo nuevamente."))

if __name__ == "__main__":
    print(informacion("Bienvenidos al taller de ejercicos python"))
    print(" ")
    print( "Yessica Ximena Barrera Leon")
    print(" ")
    print(informacion("Ficha: 2670142"))

    menu()
