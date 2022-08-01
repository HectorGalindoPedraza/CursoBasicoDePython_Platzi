from ast import Continue


def run():
    """ for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(f'{contador} es par') """
    """ for i in range(10000):
        print(i)
        if i == 5678:
            break """

    """ for letra in texto:
        if letra == 'o':
            break
        print(letra) """
    
    passSave = 'la contraseña'
    passInput = input('Ingrese la contraseña: ')
    if passInput == passSave:
        print('Contraseña Correcta!')
    else:
        while passInput != passSave:
            print('Contraseña Incorrecta!')
            break

if __name__ == '__main__':
    run()