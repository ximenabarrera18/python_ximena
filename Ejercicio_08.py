""" ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd verificar si la fecha es correcta en sentido de numero de meses y días.
"""
from Metodos import informacion,error
def val_fecha(fecha):
    try:
        año = int(fecha[:4])
        mes = int(fecha[4:6])
        dia = int(fecha[6:])
        if 1000 <= año <= 9999 and 1 <= mes <= 12 and 1 <= dia <= 31:
            return True if (mes == 2 and dia <= 29) or (mes != 2 and 1 <= dia <= 30) else False
        else:
            return False
    except ValueError:
        return False

# Ejemplo de uso
fecha_ingresada = input("Ingresa una fecha del siguiente orden año,mes,dia: ")

if val_fecha(fecha_ingresada):
    print(informacion("La fecha es válida."))
else:
    print(error("La fecha no es válida."))

    if __name__=="__main__":
        fecha_ingresada()
