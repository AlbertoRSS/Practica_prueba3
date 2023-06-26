import os
os.system("cls")
import time
from datetime import datetime




def ingresar_datos():
    registro = []
    while True:
        rut = input("Ingrese su rut:\n")
        if len(rut) >= 8 and len(rut) <= 12:
            registro.append(rut.replace(".", "").replace("-", "").lower())
            break
        else:
            print("El rut es errado")
    registro.append(input("Inserte el Nombre completo: "))
    while True:
        edad = int(input("Ingrese su edad:\n"))
        if edad > 17:
            registro.append(edad)
            break
        else:
            print("Error, debe ser mayor de edad para poder afiliarse\n")
    while True:
        estado_civil = input("Ingrese su estado civil | C = Casado, S = Soltero, V = Viudo:\n")
        if estado_civil.lower() in ["c","s","v"]:
            registro.append(estado_civil)
            break
        else:
            print("Error, al ingresar su estado civil\n")
    registro.append(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))


    return registro
