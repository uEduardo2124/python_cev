r = ''
c = me = ma = mi = 0
while r != 'N':
    c += 1
    v = int(input('Digite um valor: '))
    if c == 1:
        ma = mi = v
    else:
        if v > ma:
            ma = v
        if v < mi:
            mi = v
    me += v
    r = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
me = (me / c)
print('Você digitou {} número(s) e a média entre eles foi de {:.2f}'.format(c, me))
print('O maior valor foi {} e o menor foi {}'.format(ma, mi))
