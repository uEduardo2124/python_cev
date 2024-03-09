from datetime import date
cmaior = 0
cmenor = 0
for p in range(1, 8):
    n = int(input('Digite o ano que a {}a pessoa nasceu: '.format(p)))
    a = date.today().year
    if (a - n) >= 21:
        cmaior += 1
    else:
        cmenor += 1
print('Ao todo tiveram {} pessoas maiores de idade'.format(cmaior))
print('E também tivemos {} pessoas menores de idade'.format(cmenor))
