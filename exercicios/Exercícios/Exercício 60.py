#Versão 1.0
'''num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
contador = 1
c = num
print('Calculando {}! ='.format(num), end='  ')
while num != 1:
    if contador == 1:
        fatorial = fatorial * (num * (num - 1))
        print('{} x'.format(num), end=' ')
        num -= 1
        contador += 1
    elif contador != 1:
        fatorial = fatorial * (num - 1)
        num -= 1
    if contador == num + 1:
        print('{} '.format(num), end=' ')
    else:
        print('{} x'.format(num), end=' ')
print('= {}'.format(fatorial))'''

#Versão Guanabara com import
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} resulta em {}'.format(n, f))'''

#Versão Guanabara
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

#Versão For
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(c, 0, -1):
    print('{}'. format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
