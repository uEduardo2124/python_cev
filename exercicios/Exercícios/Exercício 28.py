from random import randint
from time import sleep
machine = randint(0, 5) # Faz a máquina "PENSAR".
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual...')
print('-=-' * 20)
player = int(input('Digite o número que acha que eu pensei: ')) # Jogador tentando adivinhar.
print('PROCESSANDO...')
sleep(3)
if player == machine:
    print('\033[32mPARABÉNS!\033[m vc conseguiu me vencer!')
else:
    print('\033[31mPERDEU!\033[m eu pensei no número {} e não no {}!'.format(machine, player))
