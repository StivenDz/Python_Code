import os
import time

#                          ESTUDIO DE FUNCIONES/PROCEDIMIENTOS Y PARAMETROS/ARGUMENTOS                               #

def saludo():
    print("Heloo Guys")

def nombre():
    name = input(" ¿Cual es tu nombre?: ")
    print("Hola un gusto conocerte",name)

def edad_question():

    name = input("¿Cual es tu nombre? ")
    edad = int(input("¿Cual es tu edad? "))

    if edad <18:
        print(f"Eres un bebe todavia, {name} tu mamá te lo limpia todavia")
    elif edad >=18 and edad<50:
        print("Bienbenid@ a la party",name)
    elif edad >=50:
        print(f"Si te cagas quien te limpia?, {name} vez a casa mejor")
    else:
        print("Sea serio, despegela mejor")

ESP = 1
ING = 2
NOS_SUBS = 3
SALIR = 4

def show_menu():
    print()
    print(f"""
                       SUBTITULOS
    {ESP})Español
    {ING})Ingles
    {NOS_SUBS})Sin subtitulos
    {SALIR})Salir                     """)



def principal():
    continuar = True
    while continuar:
        os.system('cls')
        show_menu()
        opcion = int(input("Selecciona un opcion: "))
        os.system('cls')
        if opcion == ESP:
            print("Subtitulos en Español Activado")
        else:
            if opcion == ING:
                print("Subtitulos en Ingles Activado")
            else:
                if opcion == NOS_SUBS:  
                    print("Subtitulos Desactivados")
                else:
                    if opcion == SALIR:
                        print("ok...")
                        continuar = False
                    else:
                        print("Opcion no valida...")
        input("Press enter to continue")
    print("Nos vemos care tortuga")

def saludo(nombre):
    print(f"Hola {nombre}, un gusto conocerte")

#n = input("Como te llamas? ")

def mayoria(nombre, edad):
    os.system('cls')
    print(f"Hola {nombre}, un gusto conocerte")
    print()
    print("Enseñanos la cedula para ver tu edad")
    time.sleep(4)
    print(f"Tienes {edad} años")
    if edad <18:
        print(f"Eres un bebe todavia, {nombre} tu mamá te lo limpia todavia")
    elif edad >=18 and edad<50:
        print("Bienbenid@ a la party",nombre)
    elif edad >=50:
        print(f"Si te cagas quien te limpia?, {nombre} vez a casa mejor")
    else:
        print("Sea serio, despegela mejor")

def tabla_multiplicar(numero,limite=10):
    os.system('cls')
    print(f"                  Tabla de multiplicar del {numero}")
    for i in range(1, limite +1):
        print(f"{numero} x {i} = {numero * i}")

def area_triangle(altura, base):
    return base * altura / 2

def solucion():
    altura = float(input("Ingresa la altura del triangle: "))
    base = float(input("Ingresa la base del triangle: "))
    
    print(f"Area = {area_triangle(altura, base) :.2f}")
    
def conversor_time(segundos):
    pass

if __name__ == "__main__":  #  entry point (punto de entrada)
    solucion()
    