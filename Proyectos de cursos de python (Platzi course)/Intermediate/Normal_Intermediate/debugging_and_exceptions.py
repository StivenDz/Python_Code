def divisors(num):
    divisors = []
    error = True

    while error:
        try:
            if num <= 0:
                raise ValueError("\nNo se pueden ingresar numeros menores o iguales a cero")
            elif num >0:
                for i in range (1, num + 1):
                    if num % i == 0:
                        divisors.append(i)
                error = False
                return (divisors)        
        except ValueError as ve:
            print(ve)
            if num == 0:
                print(f"el {num} no se puede dividir")
            elif num <0:
                print (f"{num} es un numero negativo")
                
            num = int(input("\nIngrese un número: "))
        

def run():
    x = True
    while x:
        try:
            num = int(input("\nIngrese un número: "))
            print(divisors(num))
            x = False
        except ValueError:
            print("Debes ingresar un numero")
        
    print()
    print("The program has finished")

#-----------------------------------------------------------------------------------------------------------------------#
def ejmp_try_except(string):
    return string == string[::-1]

def ejmp_try_except1():
    try:
        print(ejmp_try_except(1))
    except TypeError:
        print("Solo se pueden ingresar strings")
#------------------------------------------------------------------------------------------------------------------------#

def ejmp_raise(string):
    try:
        if len(string) ==0:
            raise ValueError("No se puede ingresar una caden vacía")
        else:
            return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def ejmp_raise1():
    try:
        print(ejmp_raise(""))
    except TypeError:
        print("Solo se puenen ingresar Strings")
#------------------------------------------------------------------------------------------------------------------------#

def ejmp_finally():                                 # cerrar un archivo
    try:
        f = open("archivo.txt")                     # cerrar una conexion a una base de datos
    finally:
        f.close()                                   # liberar recursos externos

def ejmp_finally1():
    pass
#------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    run()
