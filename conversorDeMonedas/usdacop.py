dolarInput = float(input('Ingrese la cantidad de dolares a convertir (USO a COP): '))
valor_Peso = 0.00023
pesos = dolarInput / valor_Peso
pesos = round(pesos, 2)
pesos = str(pesos)
print('Tiene ' + pesos + ' pesos colombianos')
