from ast import While
import os
from turtle import clear

def conversorPesosADolar(tipo_pesos, valor_dolar):
    pesosInput = float(input('¿Cuántos pesos ' + tipo_pesos + ' tienes?: '))
    dolares = pesosInput / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

def conversionDolarAPesos(valor_Peso):
    dolarInput = float(input('¿Cuántos dolares tienes?: '))
    """ valor_Peso = 0.00023 """
    pesos = dolarInput / valor_Peso
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print('Tiene ' + pesos + ' pesos colombianos')

print('\nBienvenido a este conversor de moneda!\n')

print('Elige una divisa escribiendo el numero de posicion\n')
print('1 - Pesos Colombianos')
print('2 - Pesos Mexicanos')
print('3 - Pesos Argentinos')

divisaOption = int(input('Cual vamos a convertir?: '))

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

clearConsole()

if divisaOption == 1:
    print('Elige una opcion escribiendo el número \n')
    print('1 - Convertir de pesos colombianos a dólares')
    print('2 - Convertir de dólares a pesos colombianos')
    convertOption = int(input('Escribe el número: '))
    clearConsole()
    if convertOption == 1:
        conversorPesosADolar('colombianos', 4300)
    elif convertOption == 2:
        conversionDolarAPesos(0.00023)
elif divisaOption == 2:
    print('Elige una opcion escribiendo el número \n')
    print('1 - Convertir de pesos mexicanos a dólares')
    print('2 - Convertir de dólares a pesos mexicanos')
    convertOption = int(input('Escribe el número: '))
    clearConsole()
    if convertOption == 1:
        conversorPesosADolar('mexicanos', 64)
    elif convertOption == 2: 
        conversionDolarAPesos(24)
elif divisaOption == 3:
    print('Elige una opcion escribiendo el número \n')
    print('1 - Convertir de pesos argentinos a dólares')
    print('2 - Convertir de dólares a pesos argentinos')
    convertOption = int(input('Escribe el número: '))
    clearConsole()
    if convertOption == 1: 
        conversorPesosADolar('argentinos', 65)
    elif convertOption == 2: 
        conversionDolarAPesos(65)