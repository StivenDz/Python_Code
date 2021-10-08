#FILTER /MAP /REDUCE ########### FILTER /MAP /REDUCE ############ FILTER /MAP /REDUCE ############# FILTER /MAP /REDUCE 

# high order functions == funciones de order superior
#   Es una funcion que recibe como parametro otra funcion

def saludo(func):
    func()

def hola():
    print("Hola!!!")

def adios():
    print("Adios!!!")

"""if __name__ == "__main__":
    saludo(hola)
    saludo(adios)   """

#    FILTER           FILTER          FILTER              FILTER              FILTER            FILTER        FILTER

#  HITHOUT FILTER AND WITH FILTER

def without_Filter():

    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = [i for i in my_list if i%2 != 0]   # = SIN FILTER
    print(odd)

def with_Filter():

    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x: x%2 != 0, my_list)) # = CON FILTER
    print(odd)

def reto():
    #convertir una lista del 1 al 5 en otra, pero con los numeros al cuadrado

    my_list = [1, 2, 3, 4, 5]
    
    odd1 = [i**2 for i in my_list]  # = CON LIST COMPREHENSIONS
    print(odd1)

    #odd = list(filter(lambda x: x**2, my_list))
    #print(odd)

"""if __name__ == "__main__":
    without_Filter()
    with_Filter()
    reto()"""

#    MAP           MAP          MAP              MAP              MAP            MAP        MAP        MAP          MAP


def reto_map():

    my_list = [1, 2, 3, 4, 5]

    odd1 = [i**2 for i in my_list]  # = SIN MAP
    print(odd1)

    squares = list(map(lambda x: x**2, my_list))  # = CON MAP
    print(squares)

"""if __name__ == "__main__":
    reto_map()"""

#    REDUCE          REDUCE           REDUCE            REDUCE            REDUCE            REDUCE          REDUCE        

def without_reduce():

    my_list = [2, 2, 2, 2, 2]
    all_multiplied = 1

    for i in my_list:
        all_multiplied = all_multiplied * i

    print(all_multiplied)

from functools import reduce

def with_reduce():
    
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a,b: a * b, my_list)

    print(all_multiplied)

if __name__ == "__main__":
    without_reduce()
    with_reduce()