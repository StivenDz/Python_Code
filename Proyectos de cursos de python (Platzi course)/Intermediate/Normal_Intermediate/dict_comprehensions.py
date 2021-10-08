import math


def run():
    my_dict = {}

    for i in range (1, 100):
        if i % 3 !=0:
            my_dict[i] = i**3
    print(my_dict)


def dict_comp():

    dict_comprehension = {i: i**3 for i in range(1, 100) if i % 3 !=0}
    print(dict_comprehension)

    #for keys, values in dict_comprehension.items():
        #print(f"{values}..{values}..")

def dict_reto():
    dict_reto = {i: round(math.sqrt(i),2) for i in range (1,1001)}
    print(dict_reto)

if __name__ == "__main__":
    pass