s = 0
c = 0
for n in range(1, 7):
    v = int(input('Digite o {}o. valor: '.format(n)))
    if v % 2 == 0:
        s += v
        c += 1
print('Foram informados \033[32m{}\033[m valores pares e a soma desses valores pares digitados resultou em \033[35m{}\033[m'.format(c, s))
