import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño") 
        numero_elegido = int(input("Elige otro numero: "))
    if numero_elegido == numero_aleatorio:    
        print("¡Ganaste!")          


if __name__ == "__main__":
    run()

#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.


import random

def numAleatorio():
    num = 110
    while num == 110 or num == 115 or num == 120:
        num = random.randint(100,130)

    return num   

def numeros():
    i = 0
    print()
    while True:
        a = numAleatorio()
        
        if i == 10:
            break
        elif i%2 == 0 and a%2 == 0:
            print(f"Número aleatorio   par: {a}")
            i +=1
        elif i%2 != 0 and a%2 != 0:
            print(f"Número aleatorio impar: {a}")
            i +=1

numeros()