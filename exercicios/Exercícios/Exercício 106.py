
from time import sleep
import datetime
import random
import math
c = ('\033[m',          # 0 - Sem cor
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[0;30;46m',   # 6 - Branco
     )


def linha(l, cor = 0):
    tam = len(l) + 4
    print(c[cor], end='')
    print(f'~' * tam)
    print(f'  {l}  ')
    print('~' * tam)
    print(c[0], end='')


def manual(comando, cor = 0):
    linha(f"Acessando o manual do comando '{a}'", 4)
    sleep(0.5)
    print(c[cor], end='')
    help(a)
    print(c[0], end='')
    sleep(0.5)


while True:
    linha('SISTEMA DE AJUDA PyHELP', 2)
    a = str(input('Função ou Biblioteca > ')).strip().lower()
    if a == 'fim':
        break
    else:
        manual(a, 6)
linha('ATÉ LOGO!', 1)