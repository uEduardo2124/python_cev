nome = str(input('Digite o seu nome completo: ')).strip()
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}
print('Analisando o seu nome...')
print('Seu nome em maiúsculo é {}{}{}'.format(cores['vermelho'], nome.upper(), cores['limpa']))
print('Seu nome em minúsculo é {}{}{}'.format(cores['verde'], nome.lower(), cores['limpa']))
print('Seu nome tem ao todo {}{}{} letras'.format(cores['azul'], len(nome) - nome.count(' '), cores['limpa']))
first = nome.split()
print('Seu primeiro nome é {}{}{} e ele tem {}{}{} letras'.format(cores['roxo'], first[0], cores['limpa'], cores['ciano'], len(first[0]), cores['limpa']))
