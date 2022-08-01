import random

def generar_contraseña():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', '']
    simbolos = ['!', '#', '$', '%', '/', '&', '|', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7' , '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    length = int(input(f'Ingrese la longitud que desea para la contraseña: '))

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
    password = generar_contraseña()
    print(f'\nTu nueva contraseña es: {password}')


if __name__ == '__main__':
    run()
