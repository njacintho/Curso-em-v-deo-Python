r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo.')
else:
    print('As retas não podem formar um triangulo.')
