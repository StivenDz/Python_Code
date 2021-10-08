
def registro(tipo_usuario, lista):
    print()

    while True:
        if tipo_usuario == 1:
            nombre = input("Digite el nombre del empleado: ")
            if nombre != "":
                lista.append(nombre)
            else:
                break
        else:
            nombre = input("Digite el nombre del visitante: ")
            if nombre != "":
                lista.append(nombre)
            else:
                break
    return lista

def ver_datos(tipo_usuario, lista):
    if tipo_usuario == 2:
        print("\nEmpleados registrados:")
        print(lista)
    else:
        print("\nVisitantes registrados:")
        print(lista)
    input("\nPresione enter para continuar...")

def menu():
    credenciales = ["admin", "MisionTic2021", 0]   #cambiar a 0
    datos_user   = ["",""]

    while credenciales[2] != 4:
        datos_user[0] = input("\nUsuario: ")
        datos_user[1] = input("Contraaseña: ")

        if datos_user[0] == credenciales[0] and datos_user[1] == credenciales[1]:
            break
        else:
            credenciales[2] += 1       # credenciales[2] = credenciales[2] + 1
            print("\nError, verifique sus credenciales")

    if credenciales[2] < 4:
        salir = False
        empleados = []
        visitantes = []

        while not salir:
            print("""
        +----------->BIENVENIDO<-------------+
        |                                    |
        |1. REGISTRAR EMPLEADO               |
        |2. VER EMPLEADOS REGISTRADOS        |
        |3. REGISTRAR VISITANTES             |
        |4. VER VISITANTES REGISTRADOS       |
        |0. SALIR                            |
        +------------------------------------+""")
            opcion = int(input("Digite una opción del menu: "))

            if opcion == 0:
                salir = True
            elif opcion == 1:
                empleados = registro(opcion,empleados)
            elif opcion == 2:
                ver_datos(opcion, empleados)
            elif opcion == 3:
                visitantes = registro(opcion,visitantes)
            elif opcion == 4:
                ver_datos(opcion, visitantes)
            else:
                print("\nError, opcion de menu no valida, intente de nuevo")
                input("Digite enter para continuar...")

        print("\nGracias por usar nuestro software!!")
        input("Presione enter para salir...")

if __name__ == "__main__":
    menu()