def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    palabra_invertida = word[::-1]
    print(word)
    print(palabra_invertida)
    if word == palabra_invertida:
        return True
    else:
        return False 
    

def main():
    word = input('Escribe una palabra: ')
    es_palindronmo = palindromo(word)
    if es_palindronmo == True:
        print('Es palindromo')
    else: 
        print('No es palindromo')


if __name__ == '__main__':
    main()
