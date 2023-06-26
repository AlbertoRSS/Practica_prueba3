import os
import time
os.system("cls")
from funciones import *




print("Bienvenido a Isapre “Vida y Salud” ")
time.sleep(1)
os.system("cls")


registros_isapre = []
iterar = True
while iterar == True:
    seleccion = input("""
Ingrese una opcion del menu:


1) Guardar datos de una persona
2) Buscar datos de una persona
3) Listar solo "solteros"
4)Salir del menu\n""")
    if seleccion == "1":
        registros_isapre.append(ingresar_datos())
        os.system("cls")
        print("Datos ingresados correctamente\n\nVolviendo al menu principal")
        time.sleep(2)
        os.system("cls")
    elif seleccion == "2":
        buscar = input("ingrese el rut de la persona:\n")
        encontrado = False
        for registro in registros_isapre:
            if buscar in registro:
                print(registro)
                encontrado = True
                break
        if encontrado is False:
            print("Registro no encontrado.")
            iterar = True
    elif seleccion == "3":
        buscar = input("Presione 's' para buscar personas solteras:\n")
        print("Buscando en la base las personas solteras\n")
        time.sleep(1)
        os.system("cls")
        encontrado = False
        contador_soltero = 0
        for registro in registros_isapre:
            if buscar in registro:
                contador_soltero = contador_soltero + 1
                print(registro)
                encontrado = True
        if encontrado is False:
            print("No se han encontrado personas solteras en la base")
            time.sleep(1)
            os.system("cls")
            print("Volviendo al menu prioncipal\n")
            time.sleep(1)
            os.system("cls")
        break                  
    elif seleccion == "4":
        print("Gracias por visitar Isapre “Vida y Salud” | Hasta pronto")
        time.sleep(1)
        os.system("cls")
        break
    else:
        print("Error al ingresar la opcion")
        time.sleep(1)
        os.system("cls")
        iterar = True




if seleccion == "3":
    print(f"La cantidad de pesonas solteras es: {contador_soltero}")


    edad_mayor = 0
    for registro in registros_isapre:
        for elemento in registro:
            if registro[2] > edad_mayor:
                edad_mayor = registro[2]


    print(f"La edad mayor registrada es: {edad_mayor}")
