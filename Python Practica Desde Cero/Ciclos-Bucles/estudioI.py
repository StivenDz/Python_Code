

#                                           ESTUDIO DEL WHILEEEEE                                      #

def contador():
    contador = 0
    
    while contador <= 13:
        print(f"contador: {contador}")
        contador += 1

def suma_multi():

    suma = 0
    multiplicacion = 1
    numero = -1

    while numero != 0:
        numero = int(input("Ingrese un numero (0 para salir): "))
        if numero == 0:
            print("Operaciones terminadas") 
            break
        elif numero %2 == 0:
            suma += numero
        else:
            multiplicacion *= numero
        
        print(f"Suma : {suma}")
        print(f"Multiplicacion: {multiplicacion}")

import os

def datos():
    
    USER = "stiven_dz"
    PASSWORD = "S1004360303.2021"

    user = ""
    password = ""

    while USER != user or PASSWORD != password:
        os.system('cls')
        print("            Holberton School        ")
        user = input("Usuario: ")
        password = input("Contraseña: ")

        if USER != user or PASSWORD != password:
            print("Credenciales Incorrectas")
            print("Intenta De Nuevo")
            input("Presiona Enter para continuar...")

    else:
        print("BIenvenid@")
    input("Nos Vemos Crack...")

import os

def menuPersonajes():
    
    MAGO = 1
    GUERRERO = 2
    SACERDOTISA = 3
    SALIR = 4

    continuar = True

    while continuar:
        os.system('cls')
        print(f"""    
                    Personajes

    {MAGO}) Mago
    {GUERRERO}) Guerrero    
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir   
    """)

        opcion = int(input("Selecciona tu personaje: "))

        if opcion == MAGO:
            print("""
               Mago

            Fuerza: 15
                Energia: 20
                    Especial: 12
            
            """)
        else:
            if opcion == GUERRERO:
                print("""
                Guerrero

            Fuerza: 25
                Energia: 18
                    Especial: 10 
                
                """)
            else:
                if opcion == SACERDOTISA:
                    print("""
                        Sacerdotisa

                    Fuerza: 18
                        Energia: 25
                            Especial: 22
                    
                    """)
                else:
                    if opcion == SALIR:
                        print("¡A Luchar!")
                        continuar = False
                    
                    else:
                        print("Opcion no valida")
        input("Presiona enter para continuar...")                
    
    input("Nos vemos...")

import random
import os  
def miniJogo():

    os.system("cls")
    numero_aleatorio = random.randint(1,100)
    numero_usuario_elegido = int(input("Elige un numero entre el (1-100): "))
    #maquina
    inferior = 1
    superior = 100
    maquina  = 0
    while numero_usuario_elegido != numero_aleatorio and maquina != numero_aleatorio:
        if numero_usuario_elegido != numero_aleatorio:
                #if del usuario
                if numero_usuario_elegido <=100 and numero_usuario_elegido >0:
                #os.system("cls")
                    if numero_usuario_elegido < numero_aleatorio:
                        print("-Busca un numero mas grande-")
                        if numero_usuario_elegido > inferior:
                            inferior = numero_usuario_elegido + 1
                    elif numero_usuario_elegido > numero_aleatorio:
                        print("-Busca un numero mas pequeño-")
                        if numero_usuario_elegido < superior:
                            superior = numero_usuario_elegido - 1      
                else:
                    print("""Solo numeros entre (1-100)
                              ...Pierdes tu turno...   """)
                input("Press enter to continue...")
            #numero_usuario_elegido = int(input("Elige otro numero: "))
        else:
            if numero_usuario_elegido == numero_aleatorio:
                print("¡Has Ganado!")
        #Turno de la maquina                                       Hacer Funciones
        print("\nTurno de la maquina")
        print()
        maquina = random.randint(inferior, superior)
        print(f"Numero de la maquina: {maquina}")
        if maquina < numero_aleatorio:
            print("-Busca un numero mas grande-")
            inferior = maquina + 1
        else:
            if maquina > numero_aleatorio:
                print("-Busca un numero mas pequeño-")
                superior = maquina -1
            else:
                if maquina == numero_aleatorio:
                    print()
                    print("¡Ha ganado la maquina!")
        if numero_usuario_elegido != numero_aleatorio and maquina != numero_aleatorio:
            print()
            numero_usuario_elegido = int(input("Elige otro numero: "))

    input("¡Gracias Por Jugar!")


if __name__ == "__main__":
    miniJogo()
    

    