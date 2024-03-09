frase = str(input('Digite um frase: ')).lower().strip()
cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'roxo':'\033[35m'}
print('A letra "A" aparece {}{}{} vezes na frase'.format(cores['azul'], frase.count('a'), cores['limpa']))
print('A letra "A" aparece pelo primeira vez na frase na posição {}{}{}'.format(cores['verde'], frase.find('a') + 1, cores['limpa']))
print('A letra "A" aparece por último na frase na posição {}{}{}'.format(cores['roxo'], frase.rfind('a') + 1, cores['limpa']))
