import random

def generateNewPassword():
    option = input('\n¿Desea generar otra contraseña? [Y/n]: ')
    
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
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'ch', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    simbolos = ['!', '#', '$', '%', '/', '&', '|', '(', ')', '-', '*', ';', ',', '_', '+', '[', ']', '{', '}', '´', '¨', '`', '^', '~','°', '<', '>']
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
