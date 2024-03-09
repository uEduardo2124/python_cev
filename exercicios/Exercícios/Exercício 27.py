nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'azul':'\033[34m',
         'verde':'\033[32m'}
print(cores['roxo'], 'Muito prazer em te conhecer!',cores['limpa'])
print('Seu primeiro nome é: {}{}{}'.format(cores['azul'], dividido[0], cores['limpa']))
print('Seu último nome é: {}{}{}'.format(cores['verde'], dividido[len(dividido) - 1], cores['limpa']))
