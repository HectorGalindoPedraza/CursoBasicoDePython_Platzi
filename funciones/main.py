""" def imprimirMensaje():
    print('mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')


imprimirMensaje()
imprimirMensaje()
imprimirMensaje()
 """


""" def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(mensaje)
    print('Adios')


opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
else:
    print('Escribe una opcion valida')

 """

def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado


sumatoria = suma(1, 4)
print(sumatoria)