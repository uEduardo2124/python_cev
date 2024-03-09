cont = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('')
if cont == 2:
    print('O número {} foi divisível {} vezes, e por isso ele \033[32mÉ PRIMO\033[m!'.format(n, cont))
else:
    print('O número {} foi divisível {} vezes, e por isso ele \033[31mNÃO É PRIMO\033[m!'.format(n, cont))
