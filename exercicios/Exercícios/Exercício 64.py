n = s = t = c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        t = 0
    else:
        t = n
        s += t
        c += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))

'''Resolução do Guanabara:
n = s = t = c = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(c, s))'''
