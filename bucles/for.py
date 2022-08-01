""" 
contador = 0

while contador < 100:
    if contador % 2 == 0:
        print(contador)
contador += 1 """

""" 
for contador in range(2, 1001):
    print(contador)

for i in range(10):
    print(11 * i) """


for tabla in range(1, 11):
    for val in range(1,11):
        producto = tabla * val
        print(f'{tabla} x {val} = {producto}')
        
