'''from random import randint
maior = menor = 0
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(f'{n}', end=' ')
for c in range(0, len(sorteio)):
    if c == 0:
        maior = sorteio[0]
        menor = sorteio[0]
    else:
        if sorteio[c] > maior:
            maior = sorteio[c]
        elif sorteio[c] < menor:
            menor = sorteio[c]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''

#Resolução Guanabara
from random import randint
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in sorteio:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi: {max(sorteio)}')
print(f'O menor valor sorteado foi: {min(sorteio)}')
