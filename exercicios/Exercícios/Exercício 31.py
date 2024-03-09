d = float(input('Digite a distância da sua viagem: '))
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'roxo':'\033[35m'}
print('Você está prestes a começar uma viagem de {}{}{}Km.'.format(cores['vermelho'], d, cores['limpa']))
if d > 200:
    print('E o preço da sua passagem será R${}{:.2f}{}'.format(cores['verde'], (0.45 * d), cores['limpa']))
else:
    print('E o preço da sua passagem será R${}{:.2f}{}'.format(cores['roxo'], (0.50 * d), cores['limpa']))

'''palavra = d * 0.50 if d <= 200 else d * 0.45 # Forma simplificada de condição
print('E o preço da sua passsagem será de R${:.2f}'.format(palavra))'''
