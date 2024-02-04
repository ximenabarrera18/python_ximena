"""  En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de
divisiones, operador modulo y conversión de double a entero.
"""
from datetime import datetime
from Metodos import advertencia, aviso, error, es_numero, informacion
def validar_fecha(cadena: str, formato: str= "%Y%m%d")->bool:
    try:
        fecha= datetime.strptime(cadena,formato)#Intentar convertir la cadena en objeto
        anio=fecha.year
        mes=fecha.month
        dia=fecha.day
        return True #anio,mes,dia
    except ValueError as msg_error:
        print(msg_error)
        return False

def extraer_fecha(fecha: int)->(): #tupla
    str_fecha= str(fecha)
    if len(str_fecha)==8:
        fecha=validar_fecha(fecha)
        if fecha:
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:8]
        else:
            print(advertencia(f"La cadena {str_fecha} no esta en el formato aaaammdd..."))
    else:
        print(error(f"La cadena {str_fecha} no esta en el formato aaaammdd..."))
        
        
    #Solucion sin conversion
    #Encadenamiento de comparaciones #and fecha not in [20000000, 30000000, 40000000] # %, +, -, +, /, **
    #if fecha >=10000000 and fecha<=99999999:
        #if validar_fecha(str(fecha)):
            #anio=fecha//10000 #Division entera
            #mes=(fecha%1000)//1000
            #dia= fecha % 100
            #return anio, mes, dia
    #return False
def menu_validar_fecha():
    print(aviso("Validacion de fecha (aaaammdd)"))
    numero=input(aviso(("Ingrese una fecha en el formato aaaammdd \n")))
    result=(extraer_fecha(numero))
    if result:
        print(informacion(f"el número {numero} representa la fecha {result[2]}/{result[1]}/{result[0]} que es válida"))


if __name__=="__main_":
    menu_validar_fecha()