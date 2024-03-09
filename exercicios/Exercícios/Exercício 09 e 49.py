n = int(input('Digite um número para o cálculo da sua tabuada: '))
'''cores = {'limpa':'\033[m',
         'preto':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m',
         'sublinhado':'\033[4:30m',
         'invertido':'\033[7:30m',
         'negrito':'\033[1:30m'}
print('-' * 12)
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['vermelho'], 1, cores['limpa'], cores['invertido'], (n * 1), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['verde'], 2, cores['limpa'], cores['invertido'], (n * 2), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['amarelo'], 3, cores['limpa'], cores['invertido'], (n * 3), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['azul'], 4, cores['limpa'], cores['invertido'], (n * 4), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['roxo'], 5, cores['limpa'], cores['invertido'], (n * 5), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['ciano'], 6, cores['limpa'], cores['invertido'], (n * 6), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['cinza'], 7, cores['limpa'], cores['invertido'], (n * 7), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['sublinhado'], 8, cores['limpa'], cores['invertido'], (n * 8), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['invertido'], 9, cores['limpa'], cores['invertido'], (n * 9), cores['limpa']))
print('{}{}{} x {}{:2}{} = {}{:2}{}'.format(cores['sublinhado'], n, cores['limpa'], cores['negrito'], 10, cores['limpa'], cores['invertido'], (n * 10), cores['limpa']))
print('-' * 12)'''

#Versão 2.0
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, (n * c)))
