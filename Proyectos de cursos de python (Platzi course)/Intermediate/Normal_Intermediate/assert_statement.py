def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return (divisors)        

def run():
    num = (input("\nIngrese un número: "))
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("The program has finished")
    

if __name__ == "__main__":
    run()
