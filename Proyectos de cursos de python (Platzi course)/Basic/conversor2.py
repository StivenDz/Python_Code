dolares = input("¿Cuantos dolares estadounidenses tienes?: ")
dolares = float(dolares)
valor_peso_colombiano = 3689
pesos = dolares * valor_peso_colombiano
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos colombianos ")
