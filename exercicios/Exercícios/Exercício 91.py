from random import randint
from time import sleep
from operator import itemgetter
dado = {}
ranking = []
for c in range(0, 4):
    dado[f'jogador{c + 1}'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in dado.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-=' * 30)
print('     ==', ' RANKING DOS JOGADORES ', '== ')
ranking = sorted(dado.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'    {i + 1} lugar: {v[0]} com {v[1]}')
    sleep(1)

#Na resolução do Guanabara apenas muda na coleta de dados para o dicionário de dados que foi:
#dado = {'jogador1': randint(1, 6)
#        'jogador2': randint(1, 6)
#        'jogador3': randint(1, 6)
#        'jogador4': randint(1, 6)}