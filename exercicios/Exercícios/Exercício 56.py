mi = 0
mv = 0
mvn = ''
cf = 0
for p in range(1, 5):
    print('-' * 10, '{}a PESSOA'.format(p), '-' * 10)
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M\F]: ')).strip().upper()
    if s == 'M' and i > mv:
        mv = i
        mvn = n
    elif s == 'F' and i < 20:
        cf += 1
    mi += i
mf = (mi / 4)
print('A média de idade do grupo é de {} anos'.format(mf))
print('O homem mais velho tem {} anos e se chama {}'.format(mv, mvn))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cf))
