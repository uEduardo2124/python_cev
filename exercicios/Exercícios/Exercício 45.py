from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

p = int(input('Digite a sua jogada: '))
print('JO')
sleep(1)
print('KEN')* 12
sleep(1)
print('PO!!!')

print('-=-' * 12)
print(f'Computador jogou: {itens[c]}')
print(f'Jogador jogou: {itens[p]}')
print('-=-' * 12)

if c == 0:                                  #máquina jogou pedra
    if p == 0:                              #jogador jogou pedra
        print('\033[33mEmpate\033[m!')
    elif p == 1:                            #jogador jogou papel
        print('\033[32mJOGADOR VENCEU\033[m!')
    elif p == 2:                            #jogador jogou tesoura
        print('\033[31mCOMPUTADOR VENCEU\033[m!')
    else:
        print('\033[7:mJOGADA INVÁLIDA\033[m')
elif c == 1:                                #máquina jogou papel
    if p == 0:                              #jogador jogou pedra
        print('\033[31mCOMPUTADOR VENCEU\033[m!')
    elif p == 1:                            #jogador jogou papel
        print('\033[33mEMPATE\033[m!')
    elif p == 2:                            #jogador jogou tesoura
        print('\033[32mJOGADOR VENCEU\033[m!')
    else:
        print('\033[7:mJOGADA INVÁLIDA\033[m')
else:                                       #máquina jogou tesoura
    if p == 0:                              #jogador jogou pedra
        print('\033[32mJOGADOR VENCEU\033[m!')
    elif p == 1:                            #jogador jogou papel
        print('\033[31mCOMPUTADOR VENCEU\033[m!')
    elif p == 2:                            #jogador jogou tesoura
        print('\033[33mEMPATE\033[m!')
    else:
        print('\033[7:mJOGADA INVÁLIDA\033[m')
