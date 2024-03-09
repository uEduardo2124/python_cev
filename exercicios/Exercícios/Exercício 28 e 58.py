#Versão 1.0
'''from random import randint
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
    print('\033[31mPERDEU!\033[m eu pensei no número {} e não no {}!'.format(machine, player))'''

#Versão 2.0
from random import randint
print('Olá, sou seu computador!')
m = randint(0, 10) # Faz a máquina pensar
print('Acabei de pensar em um número entre 0 e 10, tente adivinhar qual!')
p = -1
c = 0
while m != p:
    p = int(input('Digite seu palpite: '))
    if m > p:
        print('\033[31mMais...tente mais uma vez\033[m')
        c += 1
    elif m < p:
        print('\033[34mMenos...tente mais uma vez\033[m')
        c += 1
if m == p:
    c += 1
    print('\033[32mAcertou com {} tentativas. Parabéns!\033[m'.format(c))

#Resolução do Guanabara
'''from random import randint
m = randint(0, 10)
print('Olá, sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar qual foi!')
a = False
contador = 0
while not a:
    n1 = int(input('Digite seu palpite: '))
    contador += 1
    if m == n1:
        a = True
    elif m > n1:
        print('Mais...tente mais uma vez!')
    elif m < n1:
        print('Menos...tente mais uma vez!')
print('Acertou com {} tentativas, parabéns!'.format(contador))'''
