import os
import time

#                            ESTUDIO   DE    FOR    PERRACO                               #

def contador():
    for i in range(13+1):
        print(i)


def pares():

    for i in range(2,21):
        if i %2==0:
            print(i)
        
    for j in range(1, 11):
        print(f"par: {j*2}")

    for p in range (2 ,21, 2):
        print(p)


import os
import time
def regresiva():

    for temp in range(10, -1, -1):
        os.system('cls')
        print(temp)
        time.sleep(1)

    else:
        print("Feliz año nuevo")

import os
def tablas():
    os.system('cls')
    numero = int(input("¿De que numero deseas ver las tablas de multiplicar?: "))
    limite = int(input("\n¿Hasta que multiplo deseas ver?: "))
    os.system('cls')
    print(f"        Tablas del {numero}")

    for multiplo in range(1, limite + 1):
        print(f"{numero} x {multiplo} = {numero * multiplo}")

    print("Listo, Paganos")
    input("Press enter to finish the process")

import os
def tablasCompletas():
    
    for numero in range(1, 11):
        os.system('cls')
        print(f"           Tablas de multiplicar del {numero}           ")
        for multiplo in range(1, 11):
            print(f"{numero} x {multiplo} = {numero * multiplo}")
        input("Press enter to continue...")
    print("Listo crack")
    input("Press enter to leave...")

def frase():
    
    frase = input("Ingresa tu frase: ")

    for letra in frase:
        print(f"{letra}")
    
def promedio():
    
    acumulador = 0
    print("Vamos a calcular el promedio")
    total_datos = int(input("¿Cuantos datos deseas registrar?: "))

    for valor in range(total_datos):
        numero = int(input(f"Ingresa el valor {valor+1}: " ))
        acumulador += numero

    promedio = acumulador /total_datos
    promedio = round(promedio, 2)

    print(f"El promedio es: {promedio}")
    print()
    input("Press enter to leave")


def cronometro():

    for hora in range (24):
        for minuto in range (60):
            for segundo in range(60):
                os.system('cls')
                print(f"{hora}:{minuto}:{segundo}")
                time.sleep(1)
    

if __name__ == "__main__":
    cronometro()
