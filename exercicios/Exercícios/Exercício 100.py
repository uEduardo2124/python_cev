from time import sleep
from random import randint
def sorteio(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range (0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[cont]} ', end='')
        sleep(0.3)
    print('PRONTO!')

def pares(nums):
    soma = 0
    for cont in nums:
        if cont % 2 == 0:
            soma += cont
    print(f'Somando os valores pares de {nums}, temos {soma}')


nums = []
sorteio(nums)
pares(nums)
