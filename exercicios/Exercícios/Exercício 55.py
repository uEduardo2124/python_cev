maior = 0
menor = 0
for i in range(1, 6):
    p = float(input('Peso da {}a pessoa: '.format(i)))
    if i == 1:
        maior = p
        menor = p
    else:
        if menor > p:
            menor = p
        elif maior < p:
            maior = p
print('O maior peso lido foi de \033[32m{}\033[mKg'.format(maior))
print('O menor peso lido foi de \033[31m{}\033[mkg'.format(menor))
