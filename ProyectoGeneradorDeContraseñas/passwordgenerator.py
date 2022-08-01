import random

def generateNewPassword():
    print('\n¿Desea generar otra contraseña?\n')
    option = input('Escribe [Y/n]: ')
    if(option == 'Y' or option == '' or option == 'y'):
        printPassword()
        generateNewPassword()
    elif option == 'n' or option == 'N':
        exit()
    else:
        print('\nEscriba una opcion correcta!')
        generateNewPassword()


def printPassword():
    password = generar_contraseña()
    print(f'\nTu nueva contraseña es: {password}')


def generar_contraseña():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', '']
    simbolos = ['!', '#', '$', '%', '/', '&', '|', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7' , '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    length = int(input(f'\nIngrese la longitud que desea para la contraseña: '))

    for i in range(length):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password


def run():
    print("""
        Este es un generador de contraseñas
        ------------------------------------
    """)
    printPassword()
    generateNewPassword()


if __name__ == '__main__':
    run()
