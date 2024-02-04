def val_numero(valor):
    while True:
        try:
            numero = int(valor)
            return numero
        except ValueError:
            print(error("Por favor, ingrese un número válido."))
            print(advertencia("Intente nuevamente: "))
            valor = input("Ingrese nuevamente: ")


def val_float(valor):
    while True:
        try:
            numero = float(valor)
            return numero
        except ValueError:
            print(error("Por favor, ingrese un número válido."))
            print(advertencia("Intente nuevamente: "))
            valor=float(input())


        
def texto_color(texto:str, color:str):     
    ascii_color = "\033[39m {}\033[00m"
    if color == "negro":
        ascii_color = "\033[30m {}\033[00m"
    elif color == "rojo_oscuro":
        ascii_color = "\033[31m {}\033[00m"
    elif color == "verde_oscuro":
        ascii_color = "\033[32m {}\033[00m"
    elif color == "amarillo_oscuro":
        ascii_color = "\033[33m {}\033[00m"
    elif color == "azul_oscuro":
        ascii_color = "\033[34m {}\033[00m"
    elif color == "magenta_oscuro":
        ascii_color = "\033[35m {}\033[00m"
    elif color == "cyan_oscuro":
        ascii_color = "\033[36m {}\033[00m"
    elif color == "gris":
        ascii_color = "\033[37m {}\033[00m"
    elif color == "gris_oscuro":
        ascii_color = "\033[90m {}\033[00m"
    elif color == "rojo":
        ascii_color = "\033[91m {}\033[00m"
    elif color == "verde":
        ascii_color = "\033[92m {}\033[00m"
    elif color == "amarillo":
        ascii_color = "\033[93m {}\033[00m"
    elif color == "azul":
        ascii_color = "\033[94m {}\033[00m"
    elif color == "magenta":
        ascii_color = "\033[95m {}\033[00m"
    elif color == "cyan":
        ascii_color = "\033[96m {}\033[00m"
    elif color == "blanco":
        ascii_color = "\033[97m {}\033[00m"
    return ascii_color.format(texto)


def informacion(texto: str):
    return texto_color(texto,color="verde")

def error(texto: str):
    return texto_color(texto, color="rojo")


def advertencia(texto: str):
    return texto_color(texto, color="amarillo")

def aviso(texto: str):
    return texto_color(texto, color="azul")
