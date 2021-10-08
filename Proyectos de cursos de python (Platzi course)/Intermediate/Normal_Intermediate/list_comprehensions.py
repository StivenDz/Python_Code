

def run():
    numbers = []
    for i in range (101):

        if i % 3 != 0:
            numbers.append(i **2)

        #print(f"{i} al cuadrado = {i **2}")

    print(numbers)
    input()


def list_comp():

    list_comprehension = [i**2 for i in range(101) if i % 3 != 0]
    print(list_comprehension)

def list_reto():

    list_reto = [i for i in range (1, 10000)if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]

    print(list_reto)

"""def dict_comp():

    dict_comprehension = {
        [i for i in range (100)]:[ j**2 for j in range (100)]
    }
    for keys, values in dict_comprehension.items():
        print(f"{values}..{values}..")"""

if __name__ == "__main__":
    list_reto()