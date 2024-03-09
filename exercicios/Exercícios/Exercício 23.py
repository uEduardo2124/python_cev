num = int(input('Informe um número: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}
print('Analisando o número {}{}{}...'.format(cores['vermelho'], num, cores['limpa']))
print('Milhar: {}{:2}{}'.format(cores['verde'], m, cores['limpa']))
print('Centena: {}{:2}{}'.format(cores['azul'], c, cores['limpa']))
print('Dezena: {}{:2}{}'.format(cores['ciano'], d, cores['limpa']))
print('Unidade: {}{:2}{}'.format(cores['roxo'], u, cores['limpa']))
